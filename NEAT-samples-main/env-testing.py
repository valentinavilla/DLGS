import gym

env = gym.make("CartPole-v0")

observation = env.reset()

print(observation)
print(env.action_space)

done = False
while not done:
    observation, reward, done, _ ,_= env.step(env.action_space.sample())
    print(env.action_space.sample())

    env.render()