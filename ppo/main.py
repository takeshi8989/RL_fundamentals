import gym
from ppo import PPO

env = gym.make('LunarLander-v2')
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

agent = PPO(
    state_dim=state_dim,
    action_dim=action_dim,
    clip_epsilon=0.2,
    gamma=0.99,
    actor_lr=1e-4,
    critic_lr=1e-3,
    epochs=10,
    batch_size=64
)

agent.train(env, num_iterations=500, timesteps_per_batch=2048)
