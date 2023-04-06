let list  = ["mnu","rt", "fmr","fdkj","i"]
let getStringsizes = 
    strings => {return strings.map(string => strings.length);}

console.log(getStringsizes(list))

/*Good project two*/

let grades = [4,6,11,12,13,43]

let getNumberOfGrades = grades => grades.length;

let getSumGrades = grades => {
    let sum = 0;
    grades.forEach(sum_g => {
        sum += sum_g;
    });
    return sum;

}

let getAverage = grades  => {
    let sum = getSumgrades(grades);
    return sum / grades.length;
}

let getPassingGrades = grades => {
    grades.filter(grade => grade >= 10);
}

let FailingGrades = grades => {
    grades.filter(grade => grade < 10);
}


let getRaisedGrades = grades => {
    grades.forEach(grade => {
        if(grade + 1 > 20){
            return 20;
        }
        return grade += 1;
    });
}

/*strings*/

let gmailWithoutSpace = email => {
        return email.trim();

}

let getMessage = email => {
    if(email.endswith(".")){
        return email;
    }
    return email += ".";
    
}



let getUnit = text => {
    if(text.includes("'C")){
        return "Celsius";
    }
    return "N/A";
}

let getSlug = str => {
    slug = str.substring(0,14);
    slug.toLowerCase();
    slug.replaceAll(" ","-");
    return slug;
}

let toDos = chores => {
    let c = chores.split(",");
    return  c.length;
}

let renderTableRows = list => {
    return list.map(`<tr> <td>${list[0]}</td> 
    <td>${list[1]}</td> </tr>`).join("");
}

let option = countries => {
    return `${countries.map(country =><option value = 
    "${country.toLowerCase()}">${country}</option>}.join()`;
}

grades = [12,10,9,10,5,5]

let shouldAdjustGrades = grades => {
    return grades.some(grade => grade < 10);

}

let shouldCancelExam = grades => {
    return grades.every(grade => grade >= 18);
}

let resetGrades = grades => {
    grades.length = 0;
}

let resetFirst = grades => {
    return grades.splice(0,1);
    return grades.splice(1,1);
}
let sumNumbers = numbers => {
    let sum = grades.reduce((total,current) => {
    return total + current;
    
    },0);
    return sum;
}


let MultiplyNumbers = grades => {
    return grades.reduce((total,current){
        return total * current;
    },1);
}

let getLocationString = location => {
    let [lat,lng] = location;
    return `${lat,lng}`
}

let getFullName = user => {
    let [fn,ln] = user;
    return `${fn} ${ln}`;
}

let getAppas = (l1,l2) => {
    let l2 = [...l1, 8];
    return l2;
};

let l_keys = {
    id: 0
};

return l_keys.length / 2
return Object.keys(l_keys).map(key => key.toLowerCase());

let logValues = l_keys => {
   Object.keys(l_keys.).forEach(key => { console.log(l_keys[key]});
}


let ucv = Object.values(l_keys).toUpperCase();


console.log({l_keys})



let {id} = l_keys;





const getFullName = user => {
    return user.info?.name
}


let user = {
    age:18,
    name:"Max"
}

let getAge = user => {
    return user.age ?? "ukbown";
}

let getFullName = user => {
    return user?.name.toLowerCase() ?? "user";
}



grades = {
    good:13
}

let getGrades = grades => {
    return grades[grades];
}


tests = [{},{}]

let getNumberOfTestsYaken = tests => {
    return tests.length;
}
let logNames = users => {
    console.log(`${user?.name} ${user?.lastname}`)
}

let GetSumOfGrades = results => {
    let sum = 0;
    results.forEach(result =>{
        sum += result.grade;
    });
    return sum;
}


let getAverAge = ages => {
    let avg = 0;
    ages.forEach(age => {
        return avg += age;
    });
    return avg = avg / ages.length;
}



let getTotalSales = users => {
    let sum = 0;
    users.forEach(user => {
        return sum += user.sale ?? 0;
    });

    return sum;

}

let getTemperatures = recordings => {
    return recordings.map(recording => recording.tmp);
}

let getFullNames = users => {
    return users.map(user => `${user.nm} ${user.lsnm}`.toUpperCase() )
    
}



courses = [{},{},{}]

let getComplCourses = courses => {
    
return courses.filter(course => course.isCompleted);
}

let getBigGroups = chats => {
    return chats.filter(chat => chat.members >= 100);
}

return grades.find(13);

let allGroupsPublic = groups => {
    return groups.every(group => group.isPublic);
}

let csv = user.filter(user => user.isVerified).map
(user => user.name).join(",");

let sumMessageCount = groups => {
    return groups.reduce((total, current) => {
            return total + current.details.MessageCount;
    });
}

console.log()



let getCartTotal = products => {
    return products.reduce((total, current) => {
        return total + (current.price * current.quality)
    },0);
}

let getProduct = products => {
    products.reduce((total, current) => {
        return total * current.value;
    },1)
}



let runCode = () => {
    try {getData()}
    catch(error){
        console.error(error);
    }
}
let showDate = () => {
    try {
        let date = getDate()
        return date
    }

    catch(error){
        return "Couldn't get date"
    }
}



let incrementAge = user => {
    return user.age += 1;
}




let verifyUser = (users, userId) => {
    let entry = users.find(user => user.id === userId);
    entry.isVerified = true;
}




let cloneApps = apps => {
    return [...apps];
    
}


let createPerson = (fn, ln) => {
    return new Person(fn, ln);
}

class User {
    constructor(fn, ln, age){
        this.fn;
        this.ln;
        this.age;

    }
}





class Todos {
    constructor(){
        this.todos = [{
            title: "Learn JavaScript",
            category: "work"
        }, {
            title: "Meditate",
            category: "personal"
        }];     
        }


        getAll(){
            return this.todos;
        }


        getCount(){
            return this.todos.length;

        }

        add(title, category){
            this.todos.push(title, category);
        }

        getWork(){
            return this.todos.filter(todo => todo.category === "work");
        }

        getWorkCount(){
            return getWork().length;
        }

        getPersonal(){
            return this.todos.filter(todo => todo.category === "personal");
        }

        getPersonalCount(){
            return getPersonal().length;


    }
}


class Tasks {
    constructor(todos){
        this._todos;
    }

    get todos(){
        return this._todos.join(", ")
    }

}

class Payment {
    constructor(amount){
        this.amount;
    }

    get amount(){
        return this._cents;
    }

    set amount(value){
        this._cents = value * 100;
    }

}

class Discount {
    constructor() {
        this.amount = 1000;

    }

    applyDiscount(){
        if(Discount.isValid()){
            this.amount = 500;
        }
        return this;
    }

    static isValid() {
        return Math.random <= 0.5;
        return this;

    }


}

Discount.isValid().applyDiscount()



class User {
    constructor(fn,ln,age){
        this.fn
        this.ln
        this.age
    }

    canVote() {
        return this.age >= 18;
    }

    getFullName() {
        return `${fn} ${ln}`
    }

}

class Afmin extends User {
    updateConfig() {
        alert("Config updated");
    }
}




class Android {
    constructor(company,price){
        this.company
        this.price
    }

    getDescription(company, price){
        return `The ${this.company} costs ${this.price}`;
    }

    getVersion(){
        return 12;
    }


}

class iOS extends MobilePhone{
    getVersion() {
        return 15;
    }
}




function User(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
}

// This has to be a function (not an arrow function)
User.prototype.getFullName = function() {
    return `${this.firstName} ${this.lastName}`;
}

// This has to be a function (not an arrow function)
User.prototype.canVote = function() {
    return this.age >= 18;




let secEl = () => {
setTimeOut(()=>{
    console.log("1 second elapsed");
},1000);
}

const init = () => {
    fakeFetch().then(() => {
        console.log("ffc")
    });


}

const logUserDetails = () => {
    fakeFetch("user-details")
         .then(data => {
         console.log(data)
    })
     .catch(error => {
         console.error(error);
     });
 }

resolve()

reject()















































































































































































































































































































































































