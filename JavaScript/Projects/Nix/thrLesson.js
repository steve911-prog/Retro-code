/*let json = { gah: "gghbjks.jgk" };
JSON.stringify(json);
console.log(json);
let r = JSON.parse('{"gah": "nhuihgoiurseh"}');
console.log(r);
*/

//console.log([1, 2, 3, 4, 5].reduce((a, b) => (a || 0) + b));

//let list = [1, 2, 3, 4, 5];

//console.log(list.reduce((total, i) => total + i * 2));

//3 persons

let a = {
  name: "John",
  surname: "Stivens",
  age: 16,
};

let b = {
  name: "Jake",
  surname: "Johns",
  fathername: "Putinich",
};

let c = {
  name: "Sayo",
  surname: "Hint",
  sex: "man",
};

if ("age" in a) {
  console.log("Yuhuuuuuuuuuuuuuuuuuuuuuuuuu!!!");
}

let persons = {
  a: a,
  b: b,
  c: c,
};

/*
for (var i in persons) {
  console.log(persons[i].name, persons[i].surname);
}
*/

// loop of loop of values

let ab = document.querySelector("#a");

let bb = document.querySelector("#a");

let cb = document.querySelector("#a");

let for_html = [];

for (var key in persons) {
  var t = 1;
  for (var i in persons[key]) {
    console.log(persons[key][i]);
    if (t == 1 || t == 4 || t == 7) {
      ab.innerHTML += `<th>${persons[key][i]}</th>`;
    }

    if (t == 2 || t == 5 || t == 6) {
      bb.innerHTML += `<td>${persons[key][i]}</td>`;
    }

    if (t == 3 || t == 5 || t == 8) {
      cb.innerHTML += `<td>${persons[key][i]}</td>`;
    }
  }
  vart += 1;
}

//fullName
/*
for (let i in persons) {
  console.log(`${persons[i].name} ${persons[i].surname}`);
}
*/

//serialize
//console.log(JSON.stringify(persons));

//deserialize
//console.log(JSON.stringify(persons.b));
