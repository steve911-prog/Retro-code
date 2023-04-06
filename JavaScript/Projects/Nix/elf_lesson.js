// let answ = confirm("budesh keksik?");
// console.log(answ);

// switch (answ) {
//   case true:
//     console.log("ok");
// }

// +

//Switch if

// let color = prompt("Enter the color", "color");

// if (color === "red") {
//   document.write("<div style='background-color: red;'>красный</div>");
// } else if (color === "green") {
//   document.write("<div style='background-color: green;'>красный</div>");
// } else if (color === "blue") {
//   document.write("<div style='background-color: blue;'>красный</div>");
// } else if (color === "cyan") {
//   document.write("<div style='background-color: cyan;'>красный</div>");
// }

//+

//prompt: or

// let age = prompt("Age: ");
// if (age === "" || age === null || age === false) {
//   alert("Error");
//   age = age = prompt("Age: ");
// }

// //+

//confirm or this days

// let byaka = confirm("Shopping???");

// switch (byaka) {
//   case false:
//     console.log("You -> Byaka");
// }

//+

//confirm if this days

//let byaka = confirm("Shopping???");

//if (!byaka) {
//console.log("You -> Byaka");
//}

//+

//triple prompt

// let frstnme = prompt("Firstname: ");
// let lstname = prompt("Lastname: ");
// let otchs = prompt("Otchestvo: ");

// alert(frstnme, " ", lstname, " ", otchs);

//+

//default or

//let frstnme = prompt("Firstname: ");
//let lstname = prompt("Lastname: ");
//let otchs = prompt("Otchestvo: ");

//alert(`${frstnme || "Jack"} ${lstname || "Johns"} ${otchs || "Kaylovich"}`);

//+

//default if

//let frstnme = prompt("Firstname: ");
//let lstname = prompt("Lastname: ");
// let otchs = prompt("Otchestvo: ");
// let list = [frstnme, lstname, otchs];
// let names = ["Jack", "Johns", "Kaylovich"];
// let string = "";

// for (let i = 0; i < list.length; i++) {
//   if (Boolean(list[i])) {
//     string += " " + list[i];
//   } else {
//     string += " " + names[i];
//   }
// }

// alert(string);

//+

//login and pass

//let log = "admin";
//let pass = "qwerty";

//let login = prompt("Login: ");
//let pswrd = prompt("Pass: ");

//if (login === log && pswrd === pass) {
//  alert("Congratulations! :)");
//} else {
//  alert("Wrong pass or login");
//}

//+

//currecy calc

// let currency = prompt("Currency (usd or eur): ").toLowerCase();
// let buSell = confirm("If getting -> OK, if selling -> Cancel");
// let uah = prompt("UAH: ");

// switch (currency) {
//   case "usd":
//     if (buSell) {
//       console.log(uah / 32);
//     } else {
//       console.log(uah / 31.6);
//     }
//     break;
//   case "eur":
//     if (buSell) {
//       console.log(uah / 37);
//     } else {
//       console.log(uah / 39.4);
//     }
//     break;
// }

//+

//BLUE BELT

/*
let currency = prompt("Currency (usd or eur): ").toLowerCase();
let buSell = confirm("If getting -> OK, if selling -> Cancel");
let uah = prompt("UAH: ");
let course = 0;

const varOperate = (sm) => {
  course = sm;
  console.log(course);
  switch (buSell) {
    case true:
      console.log((money = uah / course));
      break;
    case false:
      console.log(uah / (course + 1));
      break;
  }
};

const gtcr = () => {
  fetch(`https://open.er-api.com/v6/latest/${currency.toUpperCase()}`)
    .then((res) => res.json())
    .then((data) => {
      console.log(data.rates.UAH);
      varOperate(data.rates.UAH);
    });
};

gtcr();
*/

//DOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONE!!!

//RoPaS

/*
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

alert("Rock: 0, Paper: 1, Scissors: 2");

let input = prompt("Enter: ");

let rndm = getRandomInt(3);
console.log(rndm);

let array = ["You", "Me", "None"];

console.log("None: ");
console.log(input == rndm);
console.log("You: ");
console.log(
  (input == 0 && rndm == 2) ||
    (input == 2 && rndm == 1) ||
    (input == 1 && rndm == 0)
);
console.log("Me:");
console.log(
  (rndm == 0 && input == 2) ||
    (rndm == 2 && input == 1) ||
    (rndm == 1 && input == 0)
);
*/
