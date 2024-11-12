export function taskFirst() {
    const task = 'I prefer const when I can.'; // Declaración con const para variable que no cambia
    return task;
  }
  
  export function getLast() {
    return ' is okay';
  }
  
  export function taskNext() {
    let combination = 'But sometimes let'; // Declaración con let para variable que se modifica
    combination += getLast();
  
    return combination;
  }
