class App {
  constructor() {
    this.navbar = document.querySelector("#btn");
    this.initEvents();
  }

  initEvents() {
    this.navbar.addEventListener("click", function(navbar) {
      console.log(this.navbar); // undefined
      /*this.navbar.remove();*/
    });
  }
}

let b = new App();
