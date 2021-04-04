# Async Await

## 정의

promise Chain으로 연결된 것을 간단하게 표현하여 동기적으로 표현되는 것처럼 보이게 만든 것

동기적으로 순서대로 보이게 만드는 것

API를 좀 더 간결하게 사용할 수 있도록 하는 것 -> Syntati Sugar

## Async

Async 를 함수 앞에 사용하면 안에 promise를 작성하지 않아도 자동으로 함수 안에 있는 코드 블록들이 promise로 반환해준다. 

```js
// async & await
// clear style of usgin promise

// 1. async
async function fetchUser() {
  // do network request in 10secs ...
  return 'jake'
};
const user = fetchUser();
user.then(console.log(user));
console.log(user);

// output
promise
jake 
```

## await

정의된 async 함수 내에서만 사용할 수 있다. 

```js
// await
function delay (ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function getApple() {
  await delay(1000);
  return 'apple'; 
}

async function getBanana() {
  await delay(1000);
  return 'banana';
}

function pickFruits() {
  try{
	  const apple = await getApple();
  	const banana = await getBanana();  
  } catch() {
  	// try catch 를 사용해 error를 핸들링할 수 있다. 이게 기존에 사용하는 코드랑 비슷하기 때문에 이해하기 쉽다. 
  }
  return '${apple} + ${banana}';
}
// 위의 코드에서 apple과 banana는 서로 연관이 없는 api 요청이다. 하지만, apple이 실행되고 1초 뒤에 banana가 실행되는 직렬형이라 비효율적이다. 이를 해결하기 위해서는 병렬형 코드를 사용하는 것이 좋다. 다음 코드를 사용하는 것이 효율적이다. 
function pickFruits() {
  const applePromise = getApple()
  const bananaPromise = getBanana()
  const apple = await applePromise;
  const banana = await bananaPromise;
  return '${apple} + ${banana}';
}
// 하지만 다음과 같은 병렬형 또한 지저분하다. 이를 해결하기 위해 다음과 같은 코드를 활용한다.

pickFruits.then(console.log())

// promise All 
function pickFruitsAll () {
  return Promise.all([getApple(), getBanana()]).then(fruits => fruits.joing('+'));
}
pickFruitsAll().then(console.log )

// output
apple + banana
```



## 참고

엘리 youtube

https://www.youtube.com/watch?v=aoQSOZfz3vQ&list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2&index=13

async await try catch를  사용해야하는 것인가?

https://velog.io/@vraimentres/async-%ED%95%A8%EC%88%98%EC%99%80-try-catch

Async await

https://velog.io/@jakeseo_me/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%9D%BC%EB%A9%B4-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0-33%EA%B0%80%EC%A7%80-%EA%B0%9C%EB%85%90-26-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-Async-Await-2bjygyrlgw