
const DisplayCategories = async () => {
  const response = await fetch("https://openapi.programming-hero.com/api/videos/categories");
  const items = await response.json();
  const categories = items.data;
  ShowingCategories(categories);
};



const ShowingCategories = (categories) => {
  const categoriesContainer = document.getElementById("categories-container");
  categories.forEach((singleCategory, index) => {
    const card = document.createElement('div');
    const btn = document.createElement('button'); 
    btn.textContent = singleCategory.category;
    btn.classList.add('category-button');

    // Check if it's the first btn
    if (index == 0) {
      btn.classList.add('active');
    }

    btn.onclick = () => {
      document.querySelectorAll('.category-button').forEach(btn => {
        btn.classList.remove('active');
      });
      btn.classList.add('active');
      singleCategoriesLoad(singleCategory.category_id);
    };
    card.appendChild(btn);
    categoriesContainer.appendChild(card); 
  });
};

let video;

const LoadSingleCategory = async (categoryId) => {
  const response = await fetch(`https://openapi.programming-hero.com/api/videos/category/${categoryId}`);
  const items = await response.json();
  const categoryItem = items.data;
  video = categoryItem;
  displaySingleCategory();
};

const totalViews = (value) => {
  let num = value.split('k')[0];
  let thousand = parseInt(num.split(".")[0]) * 1000;
  let hundred = parseInt(num.split(".")[1]) * 100;
  if (!hundred) hundred = 0;
  let totalViews = thousand + hundred;
  return totalViews;
};


let isSorted = false;

const displaySingleCategory = () => {
  const singleCategoryContainer = document.getElementById("single-category-container");
  singleCategoryContainer.textContent = "";

  const isDataFound = document.getElementById("error-message");
  if (video.length === 0) {
    isDataFound.classList.remove("hidden");
  } else {
    isDataFound.classList.add("hidden");
  }

  if (isSorted) {
    let sortedItem = video.sort((a, b) => {
      let full = totalViews(a.others.views);
      let scnd = totalViews(b.others.views);
      if (full > scnd) 
        {
        return 1;
      } 
      else 
      {
        return -1;
      }
    });
    video = sortedItem.reverse();
  }

  video.forEach((singleCategory) => {
    const totalScnd = singleCategory.others.posted_date;
    const hour = Math.floor(totalScnd / 3600);
    const remainscnd = totalScnd % 3600;
    const minit = Math.floor(remainscnd / 60);
    const card = document.createElement('div');
    const isVerified = singleCategory.authors[0].verified ? '<img class="verified-icon w-5 h-auto" src="./verify-icon.jpg" alt="Verified">' : '';
    card.innerHTML = `
    <div class="card class="h-fit rounded-lg"">

      <!-- thumbnail -->

      <figure class="w-full min-h-[100px] h-full   sm:h-[200px] relative">
        <img class="thumbnail h-full w-full rounded-md" src="${singleCategory.thumbnail}" alt="${singleCategory.title}">
        <div class="absolute bottom-3 right-3 text-white text-xs bg-[#171717] p-0.5 rounded-md">
          <span>${hour ? hour + "hrs" : ""} ${minit ? minit + "min ago" : ""}</span>
        </div>
      </figure>
      
      <!-- information -->

      <div class=" flex card-body flex-row gap-x-5 py-3">
        <div>
          <img src=" ${singleCategory.authors[0].profile_picture}" alt="${singleCategory.authors[0].profile_name}"
            class="w-10 h-10 rounded-full">
        </div>
        <div>
          <h3 class="text-xl font-semibold">${singleCategory.title}</h3>
          <div class="flex items-center gap-x-2">
            <h4 class="text-gray-500 text-base">${singleCategory.authors[0].profile_name}</h4>
            ${isVerified}
          </div>
          <h4 class="text-gray-400">${singleCategory.others.views} views</h4>
        </div>
      </div>
    </div>

      `;
    singleCategoryContainer.appendChild(card);
  });
};

const sortByView = () => {
  isSorted = true;
  displaySingleCategory();
};

DisplayCategories();
LoadSingleCategory('1000');

const handleBlog = () => {
  window.open('blog.html', '_blank');
};