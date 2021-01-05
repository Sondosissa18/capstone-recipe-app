from django.core.management.base import BaseCommand
from recipe_app.models import Recipe
from recipe_user.models import Author


class Command(BaseCommand):
    help = "will create some recipes and authors"

    def handle(self, *args, **options):

        Author.objects.bulk_create(
            [
                Author(
                    name="Jim",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Sandy",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Kelly",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Ben",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Randy",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Carey",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Jacob",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Sam",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Jill",
                    bio="Lorem ipsum dolor sit amet."
                    ),
                Author(
                    name="Jennifer",
                    bio="Lorem ipsum dolor sit amet."
                    )
            ]
        )
        Recipe.objects.bulk_create(
            [
                Recipe(
                    title="Tacos",
                    author="Jill",
                    description="These tacos are the best",
                    items="taco shells. beef. lettuce. salsa. onions.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="tacos.jpg"
                    ),
                Recipe(
                    title="Pasta",
                    author="Sam",
                    description="This pasta will blow your socks off.",
                    items="sauce. meatballs. cheese. pasta.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="pasta.jpg"
                    ),
                Recipe(
                    title="Sushi",
                    author="Jacob",
                    description="Amazing sushi with wasabi",
                    items="rice. fish. wasabi. cucumber. seaweed.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="sushi.jpg"
                    ),
                Recipe(
                    title="Fish with salad",
                    author="Sam",
                    description="Grilled fish like no other",
                    items="Fish. onion. lettuce. tomato. cucumber. ranch dressing.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="fish.jpg"
                    ),
                Recipe(
                    title="Pizza",
                    author="Kelly",
                    description="Pizza to die for with pepperoni",
                    items="Crust. cheese. sauce. pepperoni. olives.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="pizza.jpg"
                    ),
                Recipe(
                    title="Hamburger",
                    author="Jim",
                    description="Juicy burger with cheese",
                    items="Buns. hamburger. cheese. lettuce. pickles.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="hamburger.jpg"
                    ),
                Recipe(
                    title="BBQ Chicken",
                    author="Kelly",
                    description="Never ever have you tried chicken like this.",
                    items="BBQ sauce. chicken wings. ",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="chicken.jpeg"
                    ),
                Recipe(
                    title="Grilled Tofu",
                    author="Sandy",
                    description="Never say never until you try this Tofu.",
                    items="Tofu, soy sauce. rice.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="tofu.jpg"
                    ),
                Recipe(
                    title="Omelet",
                    author="Sandy",
                    description="Perfect breakfast to wake up to",
                    items="Eggs. bell pepper. onion. cilantro. sour cream.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="Omelet.jpg"
                    ),
                Recipe(
                    title="Cake",
                    author="Jim",
                    description="Jims Cake is for every birthday, and more.",
                    items="Flour. sugar. butter. vanilla. baking powder. raspberry jam.",
                    timerequired="""Excepteur sint occaecat
                                    cupidatat non proident, sunt in culpa
                                    qui officia deserunt mollit anim id est
                                    laborum.""",
                    instructions="""Duis aute irure dolor in reprehenderit
                                    in voluptate velit esse cillum dolore eu
                                    fugiat nulla pariatur.""",
                    image="cake.jpg"
                    )
            ]
        )
