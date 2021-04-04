# CallBack

정의: 파라미터로 함수를 전달하는 함수

콜백함수(Callback Function)란 **파라미터로 함수를 전달**받아, 함수의 내부에서 실행하는 함수이다.

```js
let number = [1, 2, 3, 4, 5];
number.forEach(x => {
    console.log(x * 2);
});
<output>
2
4
6
8
10
```

## 규칙

### 익명의 함수 사용

### 함수의 이름만 넘겨준다

```js
function whatYourName(name, callback) {
    console.log('name: ', name);
    callback();
}

function finishFunc() {
    console.log('finish function');
}

whatYourName('miniddo', finishFunc);

<output>
name: miniddo
finish function
```

## Callback 지옥

비동기 호출이 자주 일어나는 프로그램의 경우 '콜백 지옥'이 발생한다.
함수의 매개변수로 넘겨지는 콜백 함수가 반복되어 코드의 들여쓰기 수준이 감당하기 힘들어질 정도로 깊어지는 현상이다.

```js
function add(x, callback) {
    let sum = x + x;
    console.log(sum);
    callback(sum);
}

add(2, function(result) {
    add(result, function(result) {
        add(result, function(result) {
            console.log('finish!!');
        })
    })
})

<output>
4
8
16
finish!!
```

**해결 방안 : `Promise`를 사용하여 콜백지옥을 탈출할 수 있다.**

```js
function add(x) {
    return new Promise((resolve, reject) => {
        let sum = x + x;
        console.log(sum);
        resolve(sum);
    })
}

add(2).then(result => {
    add(result).then(result => {
        add(result).then(result => {
            console.log('finish!!');
        })
    })
})

<output>
4
8
16
finish!!
```

`Promise` 는 정상 수행 후 `resolve`, 실패 후 `reject` 가 실행된다.
`callback`을 사용했던 것과 마찬가지로 `resolve`에 값을 담아 전달한다.

하지만, 이 패턴도 그리 좋은 방법은 아니다. 결국 콜백지옥처럼 들여쓰기 수준을 감당하기 힘들어진다.

**해결 방안 : `Promise`의 return 사용하여 Promise Hell을 탈출할 수 있다.**

*프로미스를 사용하면 비동기 메서드에서 마치 동기 메서드처럼 값을 **반환**할 수 있습니다. 다만 최종 결과를 반환하지는 않고, 대신 프로미스를 반환해서 미래의 어떤 시점에 결과를 제공합니다.*

`MDN` 에서 정의하고 있는 `Promise`에 대한 설명이다.
프로미스는 비동기 호출 시, 마치 동기 호출 처럼 값을 반환할 수 있다는 문구에 집중해보자.
즉, `resolve`를 통해 전달 받은 값을 **반환**하여 사용해야 한다!

```js
function add(x) {
    return new Promise((resolve, reject) => {
        let sum = x + x;
        console.log(sum);
        resolve(sum);
    })
}

add(2).then(result => {
    return add(result);
}).then(result => {
    return add(result);
}).then(result => {
    console.log('finish!!');
})

<output>
4
8
16
finish!!
```



## 참고

https://velog.io/@minidoo/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%BD%9C%EB%B0%B1-%ED%95%A8%EC%88%98Callback-Function

https://www.youtube.com/watch?v=s1vpVCrT8f4&list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2&index=12