let result = document.getElementById('result');

function printResult(input) {
  result.innerText = '> result >>> ' + input; 
}

function twoNumberSum(array, targetSum) {
  // Write your code here.
  const arrayHashTable = new Map(); 
  console.log('hash table created'); 

  array.forEach(element => {
    if (!arrayHashTable.has(targetSum - element)) {
      arrayHashTable.set(element, true); 
    }
  });

  printResult(...arrayHashTable.entries()); 
}

twoNumberSum([1,2,3], 10);


