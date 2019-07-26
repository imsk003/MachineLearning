from IPython.display import clear_output
import numpy as np
import random
import time
import gym

env = gym.make("Taxi-v2")
env.render()

action_size = env.action_space.n 
print("Action size ", action_size) 

state_size = env.observation_space.n 
print("State size ", state_size)

qtable = np.zeros((state_size, action_size))
print(qtable)

episodes = 30000           
max_steps = 1000            
lr = 0.3                    
decay_fac = 0.00001         
gamma = 0.90 

for episode in range(episodes):
    
    state = env.reset() 
    done = False        
    lr -= decay_fac   
    step = 0
    
    if lr <= 0: 
        break
        
    for step in range(max_steps):
        
        action = env.action_space.sample()
        
        new_state, reward, done, info = env.step(action)
        
        if done == True:
            if(step < 199 | step > 201):
                qtable[state, action] = qtable[state, action]+lr*(reward+gamma*0-qtable[state,action])
            break
        else: 
            qtable[state, action] = qtable[state,action]+lr*(reward+gamma*np.max(qtable[new_state,:])-qtable[state,action])
    
        if done == True:
            break
        
        state = new_state
        
    episode += 1
    
    if (episode % 3000 == 0):
        print('episode = ', episode)
        print('learning rate = ', lr)
        print('-----------')

state = env.reset()
env.render()
done = False
total_reward = 0

while(done == False):
    
    action = np.argmax(qtable[state,:]) 
    state, reward, done, info = env.step(action) 
    total_reward += reward  
    
    time.sleep(0.5)
    clear_output(wait=True)
    env.render()
    print('Episode Reward = ', total_reward)