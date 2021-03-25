Date.prototype.yyyymmdd = function() {
    var mm = this.getMonth() + 1; // getMonth() is zero-based
    var dd = this.getDate();
  
    return [this.getFullYear(),
            (mm>9 ? '' : '0') + mm,
            (dd>9 ? '' : '0') + dd
           ].join('');
  };

function slidingWindow(m){
    const  slidingM = new Map()
    for (let i=0; i< 1000; i++){
        let sum =0;
        for(j =0;j <10;j++){
            sum +=(m.get(i+j) || 0)
        }
        slidingM.set(i,sum)
    }
    const sorted = [...slidingM.entries()].sort((a,b)=>b[1]-a[1]);
    const best = sorted[0]
    const worst = sorted[sorted.length-1]
    console.log("sequences",sorted)
    console.log("best sequence start: ",best)
    console.log("worst sequence start:",worst)
}

const reducer = (accumulator, currentValue) => accumulator + currentValue;
const sumDigits =(digit,multiplier)=> ((digit * multiplier) + "").split("").map(n=>parseInt(n))
function multiArr(i,arr){
    let count =0
    for(let i=2; i < arr.length; i++){
        const digit =parseInt(arr[i]) 
        const multiplier = i % 2 ==0 ? 2: 1
        const digits =sumDigits(digit,multiplier)
        count += digits.reduce(reducer)
    }
    return count
}
function createStats(startDate,endDate){
    const m = new Map()
    const date = new Date(startDate.getTime())
    const endValue = endDate.yyyymmdd()
    while(date.yyyymmdd() < endValue){
        console.log(date.yyyymmdd())
        const day = date.yyyymmdd();
        let count = multiArr(2,day)
        for (let i=0; i < 1000; i++){
            let lastArr = ("00" + i).split("").reverse().slice(0,3).reverse()
            let finalCount = count + multiArr(0, lastArr)
            const control = 10 - ((finalCount % 10) || 10)
            fullLast = parseInt(lastArr.join("")+control)
            m.set(fullLast,(m.get(fullLast) || 0) +1)
        }
        date.setDate(date.getDate() +1)
    }
    const sorted = [...m.entries()].sort((a, b) => (b[1] - a[1]) || (a[0]-b[0]))
    const mostCommon = sorted[0]
    const leastCommon = sorted[sorted.length -1]
    console.log({mostCommon})
    console.log({leastCommon})
    console.log("[code,occurrences]",sorted)
    slidingWindow(m)
    
    
}
createStats(new Date(1970,0,1),new Date(2002,0,1))