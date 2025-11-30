# ----------------------------------------------
# Rule-Based Expert System (Forward Chaining)
# ----------------------------------------------

class ExpertSystem:
    def __init__(self):
        self.facts = set()        # Known facts
        self.rules = []           # List of rules
        self.inference_log = []   # Store reasoning steps

    def add_rule(self, conditions, conclusion):
        """Add an IF-THEN rule to the rule base."""
        self.rules.append({"if": conditions, "then": conclusion})

    def add_fact(self, fact):
        """Add a new fact to the facts base."""
        self.facts.add(fact)

    def forward_chain(self):
        """Apply forward chaining until no new facts can be inferred."""
        added_new_fact = True

        while added_new_fact:
            added_new_fact = False
            for rule in self.rules:

                # If all conditions of a rule are satisfied
                if all(cond in self.facts for cond in rule["if"]):

                    conclusion = rule["then"]

                    # Avoid repeating facts
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        added_new_fact = True

                        # Log reasoning step
                        self.inference_log.append(
                            f"Rule fired: IF {rule['if']} THEN {conclusion}"
                        )

    def show_log(self):
        """Print all reasoning steps."""
        print("\n--- Inference Steps ---")
        for step in self.inference_log:
            print(step)

    def show_facts(self):
        print("\n--- Final Facts ---")
        for f in self.facts:
            print(f)


# ---------------------------------------------------------
# Create expert system instance and define rules
# ---------------------------------------------------------
system = ExpertSystem()

# Sample rules for a medical diagnosis system
system.add_rule(["fever", "cough"], "flu")
system.add_rule(["flu", "body_pain"], "viral_infection")
system.add_rule(["headache", "nausea"], "migraine")
system.add_rule(["red_eyes", "itching"], "allergy")
system.add_rule(["allergy", "sneezing"], "allergic_rhinitis")

# ---------------------------------------------------------
# User input section
# ---------------------------------------------------------
print("Enter your symptoms (type 'done' when finished):")

while True:
    symptom = input("Symptom: ").strip().lower()
    if symptom == "done":
        break
    system.add_fact(symptom)

# ---------------------------------------------------------
# Perform forward chaining inference
# ---------------------------------------------------------
system.forward_chain()

# Output results
system.show_log()
system.show_facts()