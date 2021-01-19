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
                    timerequired="""30 mins""",
                    instructions="""Cover and cook on Low 8 to 10 hours, or on High 4 to 5 hours. Transfer pork to a large bowl; shred using 2 forks. Add enough cooking liquid from slow cooker to moisten.""",
                    image="tacos.jpg",
                    category="DINNER",
                    ),
                Recipe(
                    title="Pasta",
                    author=Author.objects.get(username="JillPill56"),
                    description="This pasta will blow your socks off.",
                    items="sauce. meatballs. cheese. pasta.",
                    timerequired="""30 mins""",
                    instructions="""The water acts as both a cooking liquid for the noodles and the base of the sauce, while the addition of nutty Parmesan cheese at the end of cooking helps thicken the mix. Bonus: This fuss-free dinner is ready to eat in only 20 minutes.""",
                    image="pasta.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="Sushi",
                    author=Author.objects.get(username="JillPill56"),
                    description="Amazing sushi with wasabi",
                    items="rice. fish. wasabi. cucumber. seaweed.",
                    timerequired="""2 hours""",
                    instructions="""Place 1 sheet of seaweed on bamboo mat, press a thin layer of cool rice on the seaweed. Leave at least 1/2 inch top and bottom edge of the seaweed uncovered. This is for easier sealing later. Dot some wasabi on the rice. Arrange cucumber, avocado and smoked salmon to the rice. Position them about 1 inch away from the bottom edge of the seaweed.""",
                    image="sushi.jpg",
                    category="DINNER"
                    ),
                Recipe(
                    title="Fish with salad",
                    author=Author.objects.get(username="JacobWacob32"),
                    description="Grilled fish like no other",
                    items="Fish. onion. lettuce. tomato. cucumber. ranch dressing.",
                    timerequired="""a while""",
                    instructions="""Arrange blackened fillets in a single layer in the prepared baking dish, and coat with Italian-style salad dressing. Bake 30 to 35 minutes in the preheated oven, until fish is easily flaked with a fork.""",
                    image="fish.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="Pizza",
                    author=Author.objects.get(username="JacobWacob32"),
                    description="Pizza to die for with pepperoni",
                    items="Crust. cheese. sauce. pepperoni. olives.",
                    timerequired="""1 hour""",
                    instructions="""Place pizza stone on grill directly over wood fire. You may need to begin by spreading out the wood if the flames are too tall. Roll out the pizza dough to desired thickness. Place it on the pizza stone and cook 10 minutes on one side until golden.""",
                    image="pizza.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="Hamburger",
                    author=Author.objects.get(username="SammyWhammy34"),
                    description="Juicy burger with cheese",
                    items="Buns. hamburger. cheese. lettuce. pickles.",
                    timerequired="""1 hour""",
                    instructions="""Combine ground sirloin, onion, grill seasoning, liquid smoke, Worcestershire sauce, garlic, adobo sauce, and chipotle pepper in a large bowl. Form the mixture into 6 patties. Season with salt and pepper.""",
                    image="hamburger.jpg",
                    category="LUNCH"
                    ),
                Recipe(
                    title="BBQ Chicken",
                    author=Author.objects.get(username="JenniferWennifer65"),
                    description="Never ever have you tried chicken like this.",
                    items="BBQ sauce. chicken wings. ",
                    timerequired="""hour and half""",
                    instructions="""Preheat the oven to 500 degrees F (260 degrees C). In a small saucepan over medium heat, stir together the water, ketchup, brown sugar, vinegar, lemon juice, and Worcestershire sauce. Season with salt, mustard powder, and chili powder. Simmer the sauce for 15 minutes.""",
                    image="chicken.jpeg",
                    category="DINNER"
                    ),
                Recipe(
                    title="Grilled Tofu",
                    author=Author.objects.get(username="JimBoy102"),
                    description="Never say never until you try this Tofu.",
                    items="Tofu, soy sauce. rice.",
                    timerequired="""45 mins""",
                    instructions="""Cut each piece of tofu crosswise into 6 thick slices and put it all in a baking dish. Pour marinade over tofu, turning to coat, and chill, covered, turning occasionally, at least 30 minutes or up to 48 hours. Longer is better, but shorter is totally fine.""",
                    image="tofu.jpg",
                    category="DINNER"
                    ),
                Recipe(
                    title="Omelet",
                    author=Author.objects.get(username="RandyDandy43"),
                    description="Perfect breakfast to wake up to",
                    items="Eggs. bell pepper. onion. cilantro. sour cream.",
                    timerequired="""30 mins""",
                    instructions="""There are a few tricks to cooking the perfect omelet and, with practice, anyone can create a restaurant-quality omelet at home. Beginners will find it best to stick with a two-egg omelet. Once you've mastered the technique, you can move up to a three-egg omelet.""",
                    image="Omelet.jpg",
                    category="BREAKFAST"
                    ),
                Recipe(
                    title="Cake",
                    author=Author.objects.get(username="BennyLenny45"),
                    description="Jims Cake is for every birthday, and more.",
                    items="Flour. sugar. butter. vanilla. baking powder. raspberry jam.",
                    timerequired="""Not Long""",
                    instructions="""Preheat the oven to 325 °F (163 °C) and grease and flour a cake pan. Pound cakes are best baked in deep pans, such as loaf pans or bundt pans. Use butter or shortening to grease the pan. Then, sprinkle a light layer of flour into the pan, rotate the pan until it's evenly coated, then tap out the excess flour.""",
                    image="cake.jpg",
                    category="DESSERT"
                    ),
                Recipe(
                    title="Ice Cream",
                    author=Author.objects.get(username="BennyLenny45"),
                    description="Blueberry Ice cream",
                    items="cream, sugar",
                    timerequired="""2 hours""",
                    instructions="""Add all of the ingredients (except the sugar) to your blender and process until 100% smooth. Taste and if you feel you want it sweeter, add the sugar. The grapes are very sweet, so I didn't feel it was absolutely necessary but of course my daughter liked it better with the sugar.""",
                    image="blueberry.jpeg",
                    category="DESSERT"
                    ),
                Recipe(
                    title="",
                    author=Author.objects.get(username="BennyLenny45"),
                    description="",
                    items="",
                    timerequired="""Not Long""",
                    instructions="""""",
                    image="",
                    category=""
                    ),
                Recipe(
                    title="",
                    author=Author.objects.get(username="BennyLenny45"),
                    description="",
                    items="",
                    timerequired="""Not Long""",
                    instructions="""""",
                    image="",
                    category=""
                    ),
                Recipe(
                    title="",
                    author=Author.objects.get(username="BennyLenny45"),
                    description="",
                    items="",
                    timerequired="""Not Long""",
                    instructions="""""",
                    image="",
                    category=""
                    ),
                Recipe(
                    title="",
                    author=Author.objects.get(username="BennyLenny45"),
                    description="",
                    items="",
                    timerequired="""Not Long""",
                    instructions="""""",
                    image="",
                    category=""
                    ),
               ]
        )
