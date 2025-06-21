import gradio as gr
import numpy as np
import yaml
from pathlib import Path
from stable_baselines3 import PPO

# NOTE: We do not need the environment or factory for this version,
# as we will manually construct the observation array based on its known structure.

def get_run_dirs():
    """Scans the 'results' directory and returns a sorted list of valid run directories."""
    results_path = Path("results")
    if not results_path.is_dir():
        return []
    
    run_dirs = [d.name for d in results_path.iterdir() if d.is_dir() and (d / "final_model.zip").is_file()]
    run_dirs.sort(reverse=True)
    return run_dirs

# Cache for loaded models
model_cache = {}

def analyze_decision(run_dir, position, turns_remaining, turns_done, points, gems, gold, chroma, obsidian, otta, purchases):
    """
    Loads a model and predicts the action for a fully specified game state.
    """
    if not run_dir:
        return "Error: Please select a run directory."

    try:
        # --- Caching Mechanism ---
        if run_dir not in model_cache:
            print(f"Loading model for run: {run_dir}...")
            model_path = Path("results") / run_dir / "final_model"
            model = PPO.load(model_path, device="cpu")
            model_cache[run_dir] = model
        else:
            model = model_cache[run_dir]

        # --- CORRECT Observation Creation ---
        # The observation is a flattened array of features, not a dictionary of features.
        # The order must match the order in BoardGameEnv's _get_observation method.
        obs_array = np.array([
            position,
            turns_remaining,
            turns_done,
            points,
            gems,
            gold,
            chroma,
            obsidian,
            otta,
            purchases
        ], dtype=np.float32)

        # The final observation passed to the model is a dictionary with specific keys.
        observation = {
            "obs": obs_array,
            "action_mask": np.ones(6, dtype=np.int8) # For inspection, assume all actions are possible initially
        }
        
        action_map = {0: "Roll 1x", 1: "Roll 2x", 2: "Roll 3x", 3: "Roll 5x", 4: "Roll 10x", 5: "Buy Dice"}
        
        action, _ = model.predict(observation, deterministic=True)
        action_name = action_map.get(action.item(), "Unknown Action")

        return f"Agent's Decision: {action_name}"

    except Exception as e:
        if run_dir in model_cache:
            del model_cache[run_dir]
        return f"An error occurred: {e}"


# --- Create and Launch the UI ---
run_directories = get_run_dirs()

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Agent Decision Inspector")
    gr.Markdown("Select a training run and define a game state to see what action the trained agent would take.")
    
    with gr.Row():
        run_selector = gr.Dropdown(choices=run_directories, value=run_directories[0] if run_directories else None, label="Select Training Run")

    with gr.Accordion("Define Game State", open=True):
        gr.Markdown("These values must match the order in the environment's observation array.")
        with gr.Row():
            pos_input = gr.Number(value=5, label="Position")
            turns_rem_input = gr.Number(value=50, label="Turns Remaining")
            turns_done_input = gr.Number(value=0, label="Turns Done")
        with gr.Row():
            points_input = gr.Number(value=0, label="Points")
            gems_input = gr.Number(value=10, label="Gems")
            gold_input = gr.Number(value=0, label="Gold")
        with gr.Row():
            chroma_input = gr.Number(value=0, label="Chroma")
            obsidian_input = gr.Number(value=0, label="Obsidian")
            otta_input = gr.Number(value=0, label="Otta")
            purchases_input = gr.Number(value=0, label="Gem Purchases Done")

    analyze_button = gr.Button("Analyze Decision", variant="primary")
    output_text = gr.Textbox(label="Agent's Action", interactive=False)
    
    analyze_button.click(
        fn=analyze_decision,
        inputs=[run_selector, pos_input, turns_rem_input, turns_done_input, points_input, gems_input, gold_input, chroma_input, obsidian_input, otta_input, purchases_input],
        outputs=output_text
    )

if __name__ == "__main__":
    if not run_directories:
        print("Could not find any valid run directories in the 'results' folder.")
    else:
        print("Launching Gradio UI...")
        demo.launch()
