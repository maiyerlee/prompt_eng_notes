model used = gpt-3.5-turbo
endpoints = https://platform.openai.com/docs/guides/chat

Types of LLMs
- Base LLM: predicts next *word* based on *text* training data
- Instruction Tuned LLM: attempts to follow instructions
  - Reinforcement Learning with Human Feedback (RLHF)

Instruction Tuned LLM Principles:
1. Use clear and specific instructions
    - Tatics
        1. Use delimiters (indicates distinct parts of output)
            - ` ``, """, < >, <tag> </tag>, : `
        2. Ask model for a structured output
        3. Ask model to check whether conditions are satisfied
        4. "Few-shot" prompting
            - Give successful examples of completing tasks before asking model to perform the task
2. Allow time for model to process a response 
    - Tatics
        1. Specify steps required to complete a task
        2. Ask for output in a specific format
        3. Instruct the model to work out it's own solution before rushing to a conclusion

Model Limitations
- hallucinations - making statements that sounds plausible but are not true
    - model doesn't know the boundaries of it's knowledge well
    - ways to reduce hullucinations:
        - ask model to first find relevant info, then asnwer questions base on relevant info

Iterative Prompt Development
- ML: Idea -> Implementation (code/data) -> Experimental results/Error analysis -> Idea...
- Idea -> Prompt -> Results/Analysis -> Idea...
- Process: try -> analyze where model can improve on -> clarify instructions, allow model time to "think" -> refine prompts with a batch of examples

Prompt Guildlines: 
- Be clear and specific 
- Analyze why result does not give desired output
- Refine the idea and the prompt 
- Repeat 


