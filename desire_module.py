import random

class InternalStateMonitor:
    def __init__(self, initial_energy=100):
        self.energy = initial_energy
        self.threshold = 30

    def deplete_energy(self, amount=1):
        self.energy = max(0, self.energy - amount)

    def is_deprived(self):
        return self.energy <= self.threshold

    def recharge(self, amount=10):
        self.energy += amount
        self.energy = min(self.energy, 100)


class RewardSignalHandler:
    def __init__(self):
        self.reward_history = []

    def apply_reward(self, success=True):
        reward = 1 if success else -1
        self.reward_history.append(reward)
        return reward


class SpikingMotivationLoop:
    def __init__(self, state_monitor, reward_handler):
        self.state = state_monitor
        self.reward = reward_handler

    def decide_action(self):
        if self.state.is_deprived():
            return self.attempt_restore()
        return self.idle_behavior()

    def attempt_restore(self):
        success = random.random() > 0.3  # 70% chance of success
        if success:
            self.state.recharge()
        self.reward.apply_reward(success)
        return "RESTORE_SUCCESS" if success else "RESTORE_FAIL"

    def idle_behavior(self):
        self.state.deplete_energy()
        self.reward.apply_reward(False)
        return "IDLE"


# Simulated main loop
if __name__ == "__main__":
    state = InternalStateMonitor()
    reward = RewardSignalHandler()
    loop = SpikingMotivationLoop(state, reward)

    for t in range(50):
        action = loop.decide_action()
        print(f"[t={t}] Energy: {state.energy:.1f} | Action: {action}")
