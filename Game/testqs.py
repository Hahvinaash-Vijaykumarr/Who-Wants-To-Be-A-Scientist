import random

question1 = "The cycle of growth in life is know as?"
answers1 = ["A) Tricycle", "B) Life cycle", "C) Cycle", "D) Growing"]
correct1 = "B"
point1 = 1
audience1 = ["A: 1%", "B: 79%", "C: 20%", "D: 0%"]
teacher_hint1 = "Haha, are you kidding me? The answer is B!"

question2 = "Life cycle of the butterfly grows from:"
answers2 = ["A) egg-caterpillar-adult-pupa", "B) egg-caterpillar-pupa-adult", "C) adult-caterpillar-pupa-egg", "D) caterpillar-pupa-adult-egg"]
correct2 = "B"
point2 = 2
audience2 = ["A: 2%", "B: 95%", "C: 2%", "D: 1%"]
teacher_hint2 = "Come on! Im sure the answer is B!"

question3 = "The _____ is the part of the plant that makes the seed?"
answers3 = ["A) flower", "B) leaves", "C) stem", "D) roots"]
correct3 = "A"
point3 = 3
audience3 = ["A: 75%", "B: 10%", "C: 15%", "D: 0%"]
teacher_hint3 = "I think it is A. Yes, try A!"

question4 = "What is the most common gas in dry air on Earth?"
answers4 = ["A) Hydrogen", "B) Oxygen", "C) Nitrogen", "D) Neon"]
correct4 = "C"
point4 = 2
audience4 = ["A: 2%", "B: 9%", "C: 83%", "D: 6%"]
teacher_hint4 = "I am pretty sure it is C!"

question5 = "Which human body system is involved in the exchanging of gases with the surrounding?"
answers5 = ["A) Skeletal", "B) Muscular", "C) Circulatory", "D) Respiratory"]
correct5 = "D"
point5 = 2
audience5 = ["A: 0%", "B: 3%", "C: 5%", "D: 92%"]
teacher_hint5 = "Choose D!"

question6 = "Some animals are classified into four groups: insect, fish, mammal or amphibian. Which characteristic is used to classify them?"
answers6 = ["A) Type of body covering", "B) Way of producing", "C) Number of legs", "D) Way of moving"]
correct6 = "A"
point6 = 3
audience6 = ["A: 85%", "B: 3%", "C: 1%", "D: 1%"]
teacher_hint6 = "I know it is A!"

question7 = "Ali pumped more air into a ball. He observed that the size of the ball remained the same. Which of the following best explains his observations?"
answers7 = ["A) Air has mass", "B) Air occupies space", "C) Air can be compressed", "D) Air does not have definite shape"]
correct7 = "C"
point7 = 3
audience7 = ["A: 11%", "B: 8%", "C: 77%", "D: 4%"]
teacher_hint7 = "I am not sure...maybe it is C?"

question8 = "When water changes from gas to liquid at 100oC, which of the following is correct?"
answers8 = ["A) The water is boiling", "B) The water gains heat from the surroundings", "C) The water loses heat to the surroundings", "D) There is no heat gain or loss by the water"]
correct8 = "C"
point8 = 2
audience8 = ["A: 4%", "B: 10%", "C: 86%", "D: 0%"]
teacher_hint8 = "It may be C...but I am not too sure!"

question9 = "Which of the following is not correct"
answers9 = ["A) Arrows in a food chain show the flow of energy", "B) Decomposers return nutrients to the environment", "C) Energy increases as it passes through a food chain", "D) Plants convert light energy from the sun to potential energy"]
correct9 = "C"
point9 = 1
audience9 = ["A: 4%", "B: 10%", "C: 86%", "D: 0%"]
teacher_hint9 = "Well I am quite sure that it is C!"

question10 = "Which statement is correct about the mushroom and the fern?"
answers10 = ["A) Both only grow on trees", "B) Both reproduce from spores", "C) Both are non-flowering plants", "D) Both cannot make their own food"]
correct10 = "B"
point10 = 1
audience10 = ["A: 1%", "B: 90%", "C: 6%", "D: 3%"]
teacher_hint10 = "I am very sure that it is B!!"

question11 = "Which of the following is not an example of the effects of a force?"
answers11 = ["A) A piece of paper is folded into an aeroplane", "B) The seeds from a plant are dispersed by wind", "C) The temperature of a pot increases when it is heated", "D) The speed of a ball increases when it rolls down a slope"]
correct11 = "C"
point11 = 2
audience11 = ["A: 1%", "B: 6%", "C: 90%", "D: 3%"]
teacher_hint11 = "Hmm...pick C!"

question12 = "In a wooden box, objects P and Q are placed touching each other. Heat flows from P to Q. Which statements explains why heat flows?"
answers12 = ["A) P has more mass that Q", "B) P is at a higher position than Q", "C) P is at a higher temperature than Q ", "D) P is better conductor of heat than Q"]
correct12 = "C"
point12 = 2
audience12 = ["A: 1%", "B: 6%", "C: 90%", "D: 3%"]
teacher_hint12 = "I think it is C!"

question13 = "Which of the following shows the correct direction of food that is taken through the mouth?"
answers13 = ["A) stomach, small intestine, large intestine, large intestine, gullet", "B) stomach, gullet, small intestine, large intestine", "C) gullet, stomach, large intestine, small intestine", "D) gullet, stomach, small intestine, large intestine"]
correct13 = "D"
point13 = 3
audience13 = ["A: 9%", "B: 2%", "C: 6%", "D: 83%"]
teacher_hint13 = "I am confident that the answer is D!"

question14 = "How are frogs and grasshoppers similar?"
answers14 = ["A) Lays eggs", "B) Have scales", "C) Have moist skin", "D) Have a four-stage life cycle"]
correct14 = "A"
point14 = 1
audience14 = ["A: 95%", "B: 0%", "C: 0%", "D: 5%"]
teacher_hint14 = "I am pretty sure they both lay eggs! Pick A!"

question15 = "A container is used to transport heavy objects. The material for making the container must be:"
answers15 = ["A) Flexible", "B) Strong", "C) Transparent", "D) Waterproof"]
correct15 = "B"
point15 = 1
audience15 = ["A: 12%", "B: 80%", "C: 6%", "D: 2%"]
teacher_hint15 = "Well, the container has to be strong right? So I think it is B!"

# Putting the questions into an array
question_bank = [
    [question1 , answers1 , correct1, point1, audience1, teacher_hint1],
    [question2, answers2, correct2, point2, audience2, teacher_hint2],
    [question3, answers3, correct3, point3, audience3, teacher_hint3],
    [question4, answers4, correct4, point4, audience4, teacher_hint4]
    [question5, answers5, correct5, point5, audience5, teacher_hint5]
    [question6, answers6, correct6, point6, audience6, teacher_hint6]
    [question7, answers7, correct7, point7, audience7, teacher_hint7]
    [question8, answers8, correct8, point8, audience8, teacher_hint8]
    [question9, answers9, correct9, point9, audience9, teacher_hint9]
    [question10, answers10, correct10, point10, audience10, teacher_hint10]
    [question11, answers11, correct11, point11, audience11, teacher_hint11]
    [question12, answers12, correct12, point12, audience12, teacher_hint12]
    [question13, answers13, correct13, point13, audience11, teacher_hint11]
    [question14, answers14, correct14, point14, audience14, teacher_hint14]
    [question15, answers15, correct15, point15, audience15, teacher_hint15]
]
random.shuffle(question_bank) # Randomizing the question bank
def getQuestion(index):
    return question_bank[index]