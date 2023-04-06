// const { LineController } = require("chart.js");

// //assign evaluation
// var a = 5;
// var b, c;

// //b = a * 5;
// //b = c = b / 2;
// b = c = (a * 5) / 2;

// //semicolon:error
// //console.log(a;);

// //semicolon:mistake
// //there is a purose to create 'bc' variable, yet the snapshot creates
// //two vars: b and c.
// let b;
// c = 1;

// //Number:age
// let a = prompt("Age:");
// console.log(2022 - a);

// //Number: temperature
// let temperature = prompt("Enter please you temperature in 'C :");
// let farengeite = (cels) => {
//   return (cels + 1.43) / 1.1156;
// };
// farengeite(temperature);

// //Number:divide
// let divide = (one, two) => {
//   Math.floor(one, two);
// };

// //Number: odd
// const num = prompt("Enter please an odd number: ");
// let odd = Math.floor(num, 2);
// parseInt(num);
// if (parseInt(odd) === 2) {
//   alert("Correct :)");
// } else {
//   alert(":(");
// }

// //String: greeting

// alert(`Hi, ${prompt("Name: ")}`);

// //String: lexics

// let input = prompt("type the word 'Essen'");
// let rslt = input.includes("essen");
// if (rslt) {
//   alert(":)");
// } else {
//   alert("gut");
// }

// //confirm
// input = confirm("gkmrthkmnhoi;qtn;hontrn");
// typeOf(confirm());

// if (input) {
//   alert("Вы мужчина");
// } else {
//   alert("Вы женщина");
// }

// let list = [rslt, input];

// //Array: plus
// list[2] += list[1];

// // Objet: real
// let obj = {
//   height: 12,
//   width: 59504954,
// };

// //Obj. change

// obj["height"] = 2;

// obj.width = 1;

// //Comparison if

// var age = +prompt("Сколько вам лет?", "");
// if (age < 18) {
//   alert("школьник");
// } else if (age > 18 && age < 30) {
//   alert("молодеж");
// } else if (age > 30 && age < 45) {
//   alert("зрелость");
// } else if (age > 45 && age < 60) {
//   alert("закат");
// } else if (age > 60) {
//   alert("как пенсия?");
// } else if (age < 0) {
//   alert("Ty mikrob");
// } else {
//   alert("то ли киборг, то ли KERNESS");
// }

// //Comparison: sizes

// parseInt(input);
// let usatorus = (one) => {
//   return one * 6.6;
// };

// // Ternary

// input = confirm("You're man");

// if (input) {
//   alert("Oh, Man");
// } else {
//   alert("Oh, my");
// }

//Blue belt
/*let findAp = (flat, podjezd, etaj, kvartir) => {
  let house = {
    podjezd: podjezd,
    etaj: etaj,
    kvartir: kvartir,
  };
  let sum_all = podjezd * etaj * kvartir;
  let one_podjezd = sum_all / podjezd;
  let one_floor = kvartir;
  let cuurent = sum_all / podjezd;
  let podjezd_count = one_podjezd;
};

if (flat > sum_all) {
  alert(`Sorry, there's no ${flat} apartment`);
}

while (flat > podjezd_count) {
  podjezd_count += cuurent;
  if (flat <= podjezd_count) {
    podjezd_count = podjezd_count / cuurent;
    break;
  }

  let apartment = {
    podjezd: podjezd_count,
  };

  let current_floor = podjezd_count - cuurent + kvartir;

  while (flat > current_floor) {
    current_floor += kvartir;
    if (flat <= current_floor) {
      current_floor = (current_floor - podjezd_count * current) / kvartir;
      break;
    }
  }

  apartment = {
    podjezd: podjezd_count,
    floor: current_floor,
  };

  let current_apart = podjezd_count + current_floor * kvartir - one_floor;

  while (flat > current_apart) {
    current_apart += 1;
    if ((flat = current_apart)) {
      break;
    }
  }

  apartment = {
    podjezd: podjezd_count,
    floor: current_floor,
    apartment: current_apart,
  };

  console.log(apartment);
}

console.log(findAp(12333,18686,12,111));
*/
