// console.log('Start');
// setTimeout(() => {console.log("Start");}, 1000);

// new Promise((resolve, reject) => {
//     setTimeout(() => {
//         console.log("first");
//       }, 1000);
//     console.log('Inside Promise (synchronous part)');
//     resolve();
// }).then(() => {
//     console.log('Inside then (asynchronous part)');
// });

// console.log('End');
// setTimeout(() => {console.log("End");}, 1000);

for (let i = 0; i < 5; i++) {
    const randomTime = Math.floor(Math.random() * (5000 - 1000 + 1)) + 1000;
    console.log(i + ' executed after ' + randomTime + 'ms');
    setTimeout(() => {
        console.log(i);
    }, randomTime);
}

function delayLog(i) {
    return new Promise((resolve) => {
        const randomTime = Math.floor(Math.random() * (5000 - 1000 + 1)) + 1000;
        console.log(i + ' will be executed after ' + randomTime + 'ms');
        
        setTimeout(() => {
            console.log(i);
            resolve();
        }, randomTime);
    });
}

async function executeInOrder() {
    for (let i = 0; i < 5; i++) {
        await delayLog(i);
    }
}

executeInOrder();
