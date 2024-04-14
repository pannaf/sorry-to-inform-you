JOB_DESCRIPTIONS = {}
BEHAVIORS = {}
MOCK_QUESTIONS = {}
MOCK_TRANSCRIPT = {}

BEHAVIORS[
    "retail_worker"
] = """
Retail Worker

- Customer friendly
- Sociable
- Patient
- Organized
"""

JOB_DESCRIPTIONS[
    "retail_worker"
] = """
Retail Worker

• Welcoming and engaging with customers as they enter the store
• Assessing customers’ needs and suggesting solutions to their problems
• Working with cash registers and processing payments
• Setting and attaining sales goals 
• Giving customers advice about sales and promotions
• Using upselling techniques to increase store sales
• Recommending the best products to customers
• Cleaning and restocking the store throughout the day, before opening and after closing
"""

MOCK_QUESTIONS["retail_worker"] = {
    "job questions": [
        "Can you describe a time when you successfully upsold a product to a customer? How did you approach the situation and what was the outcome?",
        "Tell me about a time when you had to handle a difficult customer situation. How did you manage it and what was the result?",
        "How do you stay organized and manage your tasks throughout the day while working in a retail environment?",
    ],
    "behavior questions": [
        "Can you provide an example of a time when you demonstrated patience and understanding with a customer? How did you handle the situation?",
        "How do you approach engaging and welcoming customers as they enter the store?",
        "Can you describe a situation where you had to work with a coworker to accomplish a goal? What was your role and how did you contribute to the success of the task?",
    ],
}

MOCK_TRANSCRIPT["retail_worker"] = {}
MOCK_TRANSCRIPT["retail_worker"][
    "good"
] = """
Question: Can you describe a time when you successfully upsold a product to a customer? How did you approach the situation and what was the outcome?

Answer: Certainly! During a holiday rush, I noticed a customer purchasing a coffee machine, and I recommended a premium coffee grinder that complements it. I explained the benefits of grinding their own coffee for a fresher brew, and they were so impressed with the demonstration that they purchased the grinder along with extra coffee beans, boosting the sale by over 30%.

Question: Tell me about a time when you had to handle a difficult customer situation. How did you manage it and what was the result?

Answer: I once assisted a customer who was upset about a product being out of stock. By listening empathetically and explaining the situation, I offered to check additional stock in nearby stores and found the product. The customer was relieved and grateful, and she praised our service in an online review.

Question: How do you stay organized and manage your tasks throughout the day while working in a retail environment?

Answer: I keep a prioritized task list and use a digital planner to alert me of key activities throughout the day, ensuring nothing gets overlooked. This method helps me balance customer service with restocking and other duties efficiently, keeping the store operations smooth.

Question: Can you provide an example of a time when you demonstrated patience and understanding with a customer? How did you handle the situation?

Answer: Absolutely, a customer was struggling to decide on a gift, appearing very anxious. I patiently helped them by asking thoughtful questions about the recipient’s interests, which led them to a perfect choice, and they left the store satisfied and relieved.

Question: How do you approach engaging and welcoming customers as they enter the store?

Answer: I always greet customers with a warm smile and an open posture, making eye contact and offering assistance. This approach sets a friendly tone and makes customers feel acknowledged from the moment they step in.

Question: Can you describe a situation where you had to work with a coworker to accomplish a goal? What was your role and how did you contribute to the success of the task?

Answer: In a recent inventory audit, I partnered with a coworker to systematically check and record stock levels. I took the lead on organizing the workflow and double-checking entries, which not only streamlined the process but ensured accuracy, helping us finish ahead of schedule with excellent results.
"""

MOCK_TRANSCRIPT["retail_worker"][
    "bad"
] = """
Question: Can you describe a time when you successfully upsold a product to a customer? How did you approach the situation and what was the outcome?

Answer: Well, I tried to sell an expensive blender to a customer who was looking at cheaper models, but they were not interested and seemed annoyed by the suggestion. They ended up buying the cheapest one without any add-ons.

Question: Tell me about a time when you had to handle a difficult customer situation. How did you manage it and what was the result?

Answer: There was a customer complaining loudly about a return policy, and I found it really challenging to keep calm. I ended up calling my manager to deal with it because it was getting too stressful for me to handle.

Question: How do you stay organized and manage your tasks throughout the day while working in a retail environment?

Answer: Staying organized is tough for me; I often forget where things go and what I was supposed to do next. I try to write things down, but I still end up getting sidetracked a lot, especially when it's busy.

Question: Can you provide an example of a time when you demonstrated patience and understanding with a customer? How did you handle the situation?

Answer: Once a customer kept asking a lot of questions about products that I wasn't familiar with, and it was hard to keep my patience. I just tried to answer best as I could but eventually suggested they check online for more details.

Question: How do you approach engaging and welcoming customers as they enter the store?

Answer: I'm usually busy with tasks, so I might not notice new customers right away. When I do, I give a quick hello if they're close by, but I don't usually go out of my way unless they seem like they need help.

Question: Can you describe a situation where you had to work with a coworker to accomplish a goal? What was your role and how did you contribute to the success of the task?

Answer: We had to set up a promotional display once, and I tried to help, but I wasn't sure what to do, so I mostly let my coworker handle it. I handed them things when they asked, but I didn't really get involved much.

"""


BEHAVIORS[
    "operations_manager"
] = """
Operations Manager
- Leader
- Coach
- Good on time
- Organized
- Focused
- Confident
"""
JOB_DESCRIPTIONS[
    "operations_manager"
] = """
Operations Manager

• Long-term planning to support the company’s goals
• Coordinating different teams to foster an exchange of ideas and provide cross-team learning opportunities
• Assessing and analyzing departmental budgets to find ways to optimize profitability
• Inspiring and motivating employees through positive encouragement and incentive initiatives
• Communicating with stakeholders about shifting company priorities and projects
• Identifying potential problems and points of friction and finding solutions to maximize efficiency and revenue
• Identifying opportunities to expand or shift course based on market changes
• Enforcing regulatory and safety standards

"""

MOCK_QUESTIONS[
    "operation_manager"
] = """

"""

BEHAVIORS[
    "pharmacist"
] = """
Pharmacist
- Organized
- Efficient
- Fast
- Customer-support
- Math
- Cautious
"""

JOB_DESCRIPTIONS[
    "pharmacist"
] = """
Pharmacist Job Description

• Receiving and filling prescriptions
• Communicating with medical professionals about patients and their medications
• Listening to patients’ reports of symptoms and provide suggestions for over-the-counter medications
• Accurately measuring, preparing and distributing proper medications to the patients that need them
• Keeping track of inventory
"""
