from shapeless import liquid

@liquid
class EAOT:
    prompts: list[str]
    population: int = None
    dev_set: int = None
    iterations: int = None
    
    def run(self, prompt):
        initial_eval_scores = self.evaluate(self.prompts)

        for t in range(self.iterations):
            parent_prompts = self.select(self.prompts)
            new_prompt = self.evo(parent_prompts)
            new_score = self.evaluate(new_prompt)
            self.update(new_prompt, new_score)
        
        best_prompt = self.get_best_prompt()
        return best_prompt
    
    def evaluate(self, prompts):
        pass

    def select(self, prompts):
        pass

    def evo(self, parent_prompts):
        pass

    def update(self, new_prompt, new_score):
        pass

    def get_best_prompt(self):
        pass