//html tree
/*let body = {
  tagName: "body",
  subTags: [
    {
      tagName: "div",
      subTags: [
        {
          tagName: "span",
          text: "Enter a data plese:",
        },
        {
          tagName: "input",
          attrs: {
            type: "text",
            id: "name",
          },
        },
        {
          tagName: "input",
          attrs: {
            type: "text",
            id: "surname",
          },
        },
      ],
    },

    {
      tagName: "div",
      subTags: [
        {
          tagName: "button",
          text: "ok",
          attrs: {
            id: "ok",
          },
        },
        {
          tagName: "button",
          text: "cancel",
          attrs: {
            id: "cancel",
          },
        },
      ],
    },
  ],
};
*/

/*
//declarative fields
confirm("Enter the info about book: ");
let book = {
  name: prompt("Title:"),
  author: prompt("Author: "),
  year: Number(prompt("Year: ")),
  pages: Number(prompt("Pages: ")),
};

console.log(book);
*/

//imperative array fill 3
/*
let ar = [];

ar[0] = prompt("1: ");
ar[1] = prompt("2: ");
ar[2] = prompt("3: ");

console.log(ar);
*/

//while confirm
/*
let c = confirm("Decide");

while (c == false) {
  c = confirm("Decide");
  if (c == true) {
    break;
  }
}
*/

//array fill
/*
let c = confirm("Decide");
let d = [];

while (c == true) {
  c = confirm("Decide");
  d.push(1);
  if (c == false) {
    console.log(d);
    break;
  }
}
*/

//array fill nopush
/*
let c = confirm("Decide");
let a = -1;
let d = [];

while (c == true) {
  c = confirm("Decide");
  a += 1;
  d[a] = 1;
  if (c == false) {
    console.log(d);
    break;
  }
}
*/

//infinite probability
/*
let rnd = Math.random();
let i = 0;
while (rnd < 0.9) {
  i += 1;
  console.log(rnd);
  rnd = Math.random();
  if (rnd > 0.9) {
    console.log(i);
    break;
  }
}
*/

//empty loop
/*
let p = prompt("None");

alert(p);

while (p == null) {
  p = prompt("None");
}
*/

//progression sum
/*
let r = 0;

for (i = 1; i < 1000; i += 3) {
  r += i;
}

console.log(r);
*/

//chess one line
/*
let line = "";

for (i = 1; i < 23; i++) {
  line += " #";
}

line += " o";
console.log(line);
*/

//numbers
/*
let n = "";

for (i = 0; i < 23; i++) {
  for (i = 0; i < 10; i++) {
    n += i;
  }
  n += "\n";
  console.log(n);

}
*/

//chess
/*let a = "";

for (i = 1; i < 7; i++) {
  a += ".#";
}

a += "\n";

for (i = 1; i < 7; i++) {
  a += "#.";
}

a += "\n";
let b = a;
console.log(a);

for (i = 1; i != 12; i++) {
  a += b;
}

console.log(a);
*/

//cubes
/*let a = [];

for (i = 0; i != 13; i++) {
  a.push(i * i * i);
}

console.log(a);
*/

//multiply table
/*let a = [0];

for (i = 1; i != 10; i++) {
  a[i] = [];

  for (b = 1; b != 10; b++) {
    a[i].push(i * b);
  }
}

a.shift();

console.log(a);
*/

//Blue BELT -. triangle
/*

let a = ".....";
let b = "#";
let c = "";

for (i = 1; i != 7; i++) {
  c = a + b + a;
  console.log(c);
  b += "##";
  a = a.replace(".", "");
}*/

//Black BElt
/*let a = Number(prompt("Number: "));

let h = [];

for (i = 1; i != 100; i++) {
  a = Number(prompt("Number: "));

  if (i > 4) {
    a[0].shift();
  }

  h.push(a);

  if (i % 4 === 0) {
    let c = confirm("Continue or exit???");
    if (c === false) {
      break;
    }
  }

  alert(h);
}*/
