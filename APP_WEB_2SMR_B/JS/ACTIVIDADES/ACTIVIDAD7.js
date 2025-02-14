document.addEventListener("DOMContentLoaded",function(){
   const pre = parseInt(prompt("Selecione el numero deseado: Celsius-->Fahrenheit = 1 Fahrenheit-->Celsius = 2"))
    let cel;
    let cal_cel;
    let fahr;
    let cal_fahr;
   
    if (pre == 1){
        cel = parseFloat(prompt("Introduce la temperatura en grados Celsious"));
        cal_cel = cel * 9/5 + 32;
        alert(cal_cel);
    }
    
    if (pre == 2){
        fahr = parseFloat(prompt("Introduce la temperatura en grados Fahrenheit"));
        cal_fahr = (fahr - 32)*5/9;
        alert(cal_fahr);
    }
});