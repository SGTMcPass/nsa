import ray
from ray.rllib.algorithms.ppo import PPOConfig

print("--- Inspecting Default PPOConfig for Ray RLlib ---")

try:
    # 1. Instantiate the specific PPOConfig object. This is the correct modern API.
    default_config = PPOConfig()

    print("\n--- Valid Hyperparameters for the .training() method ---")
    
    # 2. The training parameters are attributes of the config object.
    #    We can inspect the object to find all valid keys.
    #    We filter out private/internal attributes that start with '_'.
    for key in sorted(default_config.to_dict().keys()):
        if not key.startswith('_'):
            print(key)

    print("\n----------------------------------------------------")
    print("\nSUCCESS: Inspection complete. Use one of the keys from the list above for the GAE-Lambda parameter in your YAML file.")


except Exception as e:
    print(f"\n--- ERROR during inspection ---")
    print(f"Error: {e}")
