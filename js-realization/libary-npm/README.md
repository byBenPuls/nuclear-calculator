# Nuclear Calculator

## This simple app can give you information about a nucleus radius or information about an isotope.


```js
const nucl = require(nuclear-calculator)
console.log(nuclt.getRadius('he-4'))

// Console: 1.4943052148752003

console.log(nucl.getInfo('h-1'))

// Console: [ 'Hydrogen', 1, 1.007825031898, 0, 1, 1, true, 0.37625467857525335 ]
```
### 0 - name element
### 1 - atomic number
### 2 - mass number
### 3 - count neutrons
### 4 - count protons
### 5 - count electrons
### 6 - stable (True or False)
### 7 - nuclear radius

### Thus, you can take required value in the following way

```js
const nucl = require(nuclear-calculator)
console.log(nucl.getInfo('h-1')[0])

// Hydrogen
```