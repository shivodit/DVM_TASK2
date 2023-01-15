from django.db import models

# Create your models here.
class Question(models.Model):
    quiz = models.ForeignKey("Quiz",on_delete = models.CASCADE,related_name="questions")
    question = models.CharField("question",max_length=500)
    index = models.IntegerField("index")

    class Meta:
        ordering = ("index",)

class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE,related_name="choices")
    is_correct = models.BooleanField("is_correct",default=False)
    choice = models.CharField("Choice", max_length=50)
    position = models.IntegerField("position")

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"), 
            # no duplicated position per question 
            ("question", "position") 
        ]
        ordering = ("position",)


class Quiz(models.Model):
    title = models.CharField(max_length = 500)
    author = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name="quiz")
    pub_date = models.DateTimeField(auto_now_add=True)