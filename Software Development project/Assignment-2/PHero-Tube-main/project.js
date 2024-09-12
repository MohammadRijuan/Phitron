const LoadAllCategories = async () => {
    try 
    {
        const response = await fetch("https://openapi.programming-hero.com/api/videos/categories");
        const items = await response.json();
        const categories = items.data;
        DisplayAllCategories(categories);
    } 
    catch (error) 
    {
        console.error(error);
    }
};

const DisplayAllCategories = (categories) => {
    const CategoriesContainer = document.getElementById("category-container");
    CategoriesContainer.textContent = ""; // Clean up existing content

    categories.forEach((SingleCategory, Index) => {
        const card = document.createElement('div');
        const btn = document.createElement('button');
        btn.textContent = SingleCategory.category;
        btn.classList.add('category-btn');

        if (Index == 0) 
        {
            btn.classList.add("active");
        }

        btn.onclick = () => {
            document.querySelectorAll(".category-btn").forEach(btn => {
                btn.classList.remove("active");
            });

            btn.classList.add("active");
            LoadSingleCategories(SingleCategory.category_id);
        };

        card.appendChild(btn);
        CategoriesContainer.appendChild(card);
    });
};

let video = [];

const LoadSingleCategories = async (categoryId) => {
    try 
    {
        const response = await fetch(`https://openapi.programming-hero.com/api/videos/category/${categoryId}`);
        const items = await response.json();
        video = items.data;
        DisplaySingleCategories();
    } 
    catch (error) 
    {
        console.error(error);
    }
};

let Sorted = false;

const Views = (value) => {
    let nums = value.split('K')[0];
    let thousands = parseInt(nums.split(".")[0]) * 1000;
    let hundreds = parseInt(nums.split(".")[1]) * 100;
    
    if (!hundreds) hundreds = 0;

    let Views = thousands + hundreds;

    return Views;
};

const DisplaySingleCategories = () => {
    const SingleCategoryContainer = document.getElementById("single-category");
    SingleCategoryContainer.textContent = "";

    const FoundData = document.getElementById("err-msg");

    if (video.length == 0) 
    {
        FoundData.classList.remove("hidden");
    }
    else 
    {
        FoundData.classList.add("hidden");
    }

    if (Sorted) 
        {
        let SortedItems = video.filter(items => items.others && items.others.views) // Ensur views exist
            .sort((x, y) => 
                {
                let full = Views(x.others.views);
                let Secnd = Views(y.others.views);

                if (full > Secnd) 
                {
                    return 1;
                } 
                else 
                {
                    return -1;
                }
            });

        video = SortedItems.reverse();
    }

    video.forEach((SingleCategory) => {
        // console.log(SingleCategory);

        const TotalSecnd = SingleCategory?.others?.posted_date;
        const Hour = Math.floor(TotalSecnd / 3600);
        const RemainSecnd = TotalSecnd % 3600;
        const minit = Math.floor(RemainSecnd / 60);
        const card = document.createElement("div");

        const Verified = SingleCategory.authors && SingleCategory.authors[0]?.verified ? '<img class="verify-icon w-5" src="./verify-icon.jpg">' : '';

        

        card.innerHTML = `
            <div class="card h-fit rounded-lg">
                
                <!-- thumbnail -->

                <div class="w-full min-h-[100px] h-full sm:h-[200px] relative">
                    <img class="thumbnail h-full w-full rounded-md" src="${SingleCategory.thumbnail}" alt="${SingleCategory.title}">
                    
                    <div class="absolute bottom-3 right-3 text-white text-xs bg-[#171717] p-0.5 rounded-md">
                        <span>${Hour ? Hour + "hrs" : ""} ${minit ? minit + "min ago" : ""}</span>
                    </div>
                </div>

                <!-- information -->

                <div class=" flex card-body flex-row gap-x-5 py-3">
                    <div>
                        <img src=" ${SingleCategory.authors[0].profile_picture}" alt="${SingleCategory.authors[0].profile_name}"
                        class="w-10 h-10 rounded-full">
                    </div>
                    <div>
                        <h3 class="text-2xl font-semibold">${SingleCategory.title}</h3>

                        <div class="flex items-center gap-x-2">
                            <h4 class="text-gray-700 text-base">${SingleCategory.authors[0].profile_name}</h4><span>${Verified}</span>
                        </div>

                        <h4 class="text-gray-500">${SingleCategory.others.views} views</h4>
                
                    </div>
                </div>
            </div>
        `;
        SingleCategoryContainer.appendChild(card);
    });
};

const SortByView = () => {
    Sorted = true;
    DisplaySingleCategories();
};

LoadAllCategories();

LoadSingleCategories('1000');


const Blog =() =>{
    window.open('blog.html', '_blank');
}