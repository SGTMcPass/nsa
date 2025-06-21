import ray
from ray.rllib.algorithms.ppo import PPO

print("--- Starting RLlib minimal test ---")

try:
    # This is the same API call pattern from our rllib_runner.py
    # We get the PPO class directly, then call .get_config() on it.
    config_obj = (
        PPO.get_config()
        .environment(env="CartPole-v1") # Use a standard, simple env
        .framework("torch")
    )

    print("Successfully created config object.")

    # Build the algorithm
    algo = config_obj.build()

    print("--- SUCCESS: Successfully built PPO algorithm instance. ---")
    print(f"Algorithm class: {type(algo)}")

except Exception as e:
    print(f"\n--- ERROR: Test failed. ---")
    print(f"Error Type: {type(e)}")
    print(f"Error Message: {e}")
    # Print the traceback for detailed debugging
    import traceback
    traceback.print_exc()
finally:
    if ray.is_initialized():
        ray.shutdown()
        print("Ray shut down.")
