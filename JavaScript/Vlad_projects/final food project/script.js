// TODO
// import FetchWrapper from "./fetch-wrapper.js"
// const API = new FetchWrapper("https://firestore.googleapis.com/v1/projects/jsdemo-3f387/databases/(default)/documents/project");
const coefo = {
    carbs:{
        pizza: 16,
        pasta: 12,
        burger: 15,
        soup:  10,
        salad:  9,
        apple:  11,
        peach:  13,
        cider:   16
    },
    protein:{
        pizza:  9,
        pasta:  9,
        burger: 9,
        soup:  7,
        salad: 8,
        apple: 6,
        peach: 5,
        cider: 6
    },
    fat:{
        pizza: 13,
        pasta: 12,
        burger: 14,
        soup:  10,
        salad: 7,
        apple: 5,
        peach: 5,
        cider: 5
    }
}
let btn = document.querySelector(".btn btn-default create-submit");
let tot_cal = document.querySelector("#total-calories");
let food = document.querySelector("#create-name");
let carbs = document.querySelector("#create-carbs");
let protein = document.querySelector("#create-protein");
let fat = document.querySelector("#create-fat");
btn.addEventListener("submit",count = () =>{
        let ccal =  carbs * coefo.carbs.food + protein * coefo.protein.food + fat * coefo.fat.food;
        tot_cal.textContent = ccal;
        console.log(ccal); 
    
});

() => a+b


/*
import FetchWrapper from "./fetch-wrapper.js";

const API = new FetchWrapper(
  "https://firestore.googleapis.com/v1/projects/jsdemo-3f387/databases/(default)/documents/project"
);

const form = document.querySelector("#create-form");
const name = document.querySelector("#create-name");
const carbs = document.querySelector("#create-carbs");
const protein = document.querySelector("#create-protein");
const fat = document.querySelector("#create-fat");
const list = document.querySelector("#food_list");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  API.post("/", {
    fields: {
      name: { stringValue: name.value },
      carbs: { integerValue: carbs.value },
      protein: { integerValue: protein.value },
      fat: { integerValue: fat.value },
    }
  }).then((data) => {
    console.log(data);
    if (data.error) {
        // there was an error
        return;
    }

    

    // TODO: add new food to the list
    list.insertAdjacentHTML("beforeend",
    `<li class="card">
  <div>
    <h3 class="name">${name.value}</h3>
    <div class="calories">0 calories</div>
    <ul class="macros">
      <li class="carbs"><div>Carbs</div><div class="value">             ${carbs.value}g</div></li>
      <li class="protein"><div></div><div class="value">${protein.value}g</div></li>
      <li class="fat"><div>Fat</div><div class="value">${fat.value}g</div></li>
    </ul>
  </div>
</li>`);

    name.value = "";
    carbs.value = "";
    protein.value = "";
    fat.value = "";
  });
});
