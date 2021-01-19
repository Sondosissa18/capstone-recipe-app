from django.core.management.base import BaseCommand
from recipe_app.models import Recipe
from recipe_user.models import Author
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "will create some recipes and authors"

    def handle(self, *args, **options):
        try:
            Author.objects.bulk_create(
                [
                    Author(
                        name='Jim',
                        username="JimBoy102",
                        ),
                    Author(
                        name='Sandy',
                        username="SandyLandy134",
                        ),
                    Author(
                        name="Kelly",
                        username="KellyWelly240",
                        ),
                    Author(
                        name="Ben",
                        username="BennyLenny45",
                        ),
                    Author(
                        name="Randy",
                        username="RandyDandy43",
                        ),
                    Author(
                        name="Carey",
                        username="CareyPorey34",
                        ),
                    Author(
                        name="Jacob",
                        username="JacobWacob32",
                        ),
                    Author(
                        name="Sam",
                        username="SammyWhammy34",
                        ),
                    Author(
                        name="Jill",
                        username="JillPill56",
                        ),
                    Author(
                        name="Jennifer",
                        username="JenniferWennifer65",
                        )
                ]
            )
        except IntegrityError as e:
            print(e)
        Recipe.objects.bulk_create(
            [
                Recipe(
                    title="Tacos",
                    author=Author.objects.get(username="JillPill56"),
                    description="These tacos are the best",
                    items="taco shells. beef. lettuce. salsa. onions.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="tacos.jpg",
                    category="DINNER",
                    ),
                Recipe(
                    title="Pasta",
                    author=Author.objects.get(username="JillPill56"),
                    description="This pasta will blow your socks off.",
                    items="sauce. meatballs. cheese. pasta.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="pasta.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="Sushi",
                    author=Author.objects.get(username="JillPill56"),
                    description="Amazing sushi with wasabi",
                    items="rice. fish. wasabi. cucumber. seaweed.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="sushi.jpg",
                    category="DINNER"
                    ),
                Recipe(
                    title="Fish with salad",
                    author=Author.objects.get(username="JacobWacob32"),
                    description="Grilled fish like no other",
                    items="Fish. onion. lettuce. tomato. cucumber. ranch dressing.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="fish.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="Pizza",
                    author=Author.objects.get(username="JacobWacob32"),
                    description="Pizza to die for with pepperoni",
                    items="Crust. cheese. sauce. pepperoni. olives.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="pizza.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="Hamburger",
                    author=Author.objects.get(username="SammyWhammy34"),
                    description="Juicy burger with cheese",
                    items="Buns. hamburger. cheese. lettuce. pickles.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="hamburger.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="BBQ Chicken",
                    author=Author.objects.get(username="JenniferWennifer65"),
                    description="Never ever have you tried chicken like this.",
                    items="BBQ sauce. chicken wings. ",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="chicken.jpeg",
                    category="DINNER"
                    ),
                Recipe(
                    title="Grilled Tofu",
                    author=Author.objects.get(username="JimBoy102"),
                    description="Never say never until you try this Tofu.",
                    items="Tofu, soy sauce. rice.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="tofu.jpg",
                    category="DINNER"
                    ),
                Recipe(
                    title="Omelet",
                    author=Author.objects.get(username="RandyDandy43"),
                    description="Perfect breakfast to wake up to",
                    items="Eggs. bell pepper. onion. cilantro. sour cream.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="Omelet.jpg",
                    category="BREAKFAST"
                    ),
                Recipe(
                    title="Cake",
                    author=Author.objects.get(username="BennyLenny45"),
                    description="Jims Cake is for every birthday, and more.",
                    items="Flour. sugar. butter. vanilla. baking powder. raspberry jam.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="cake.jpg",
                    category="DESSERT"
                    )
               ]
        )
