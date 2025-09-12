'''6. Customer Feedback Analysis
Scenario:
A company collects customer feedback in the form of ratings (1-5). Write a program to
 calculate the **percentage of positive feedback** (4 or 5).
Requirements:
- Use a function to calculate the positive feedback percentage.
- Handle cases where no ratings are available.
Input Example:
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
Expected Output:
Positive Feedback: 62.5%
'''
def positive_feedback_percentage(ratings):
    if not ratings:  
        return 0
    positive = [r for r in ratings if r >= 4]
    percentage = (len(positive) / len(ratings)) * 100
    return percentage
ratings = list(map(int, input("Enter ratings (from 1-5): ").split()))
percentage = positive_feedback_percentage(ratings)
print("Positive Feedback:", round(percentage, 2), "%")
