var now = new Date(Date.now());
console.log(now);

const ends = [
    new Date(2024, 8, 20, 12, 45), // 12:45 friday sep 20th 2024
    new Date(2024, 11, 20, 12, 45),
    new Date(2025, 2, 7, 12, 45),
    new Date(2025, 4, 23, 12, 45)
];
const starts = [
    new Date(2024, 6, 23, 8, 15),
    new Date(2024, 9, 8, 8, 15),
    new Date(2025, 1, 7, 8, 15),
    new Date(2025, 2, 25, 8, 15),
    new Date(2030, 2, 25, 8, 15), // basicaly forever

];

const names = [
    "summer",
    // "fall",
    "autumn", // fall is now autumn, because it needed to match 6 character 
    "winter",
    "spring",
    "summer"
];


const holidays = [ // any holiday or day during a break
    "2024-09-02", "2024-09-23", "2024-09-24", "2024-09-25", "2024-09-26",
    "2024-09-27", "2024-09-28", "2024-09-29", "2024-09-30", "2024-10-01",
    "2024-10-02", "2024-10-03", "2024-10-04", "2024-10-05", "2024-10-06",
    "2024-10-07", "2024-11-25", "2024-11-26", "2024-11-27", "2024-11-28",
    "2024-11-29", "2024-12-23", "2024-12-24", "2024-12-25", "2024-12-26",
    "2024-12-27", "2024-12-28", "2024-12-29", "2024-12-30", "2024-12-31",
    "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05",
    "2025-01-06", "2025-01-20", "2025-02-17", "2025-03-10", "2025-03-11",
    "2025-03-12", "2025-03-13", "2025-03-14", "2025-03-15", "2025-03-16",
    "2025-03-17", "2025-03-18", "2025-03-19", "2025-03-20", "2025-03-21",
    "2025-03-22", "2025-03-23", "2025-03-24", "2025-04-18", "2025-05-26"
];

function timeIntegral(start, end){
    
    var loop_now = start.getTime();
    var total = 0;
    
    while (end.getTime() - loop_now > 0) {
        day = new Date(loop_now);
        if (holidays.includes(day.toISOString().slice(0, 10))) {
            loop_now += 24 * 60 * 60 * 1000;
            continue;
        }
        day = day.getDay();
        // console.log( loop_now,new Date (loop_now).getDay()  );
        if (0 < day && day< 5) {
            total += (7 * 60 * 60) + (45 * 60); // 7h 45m
        } else if (day === 5) {
            total += (4 * 60 * 60) + (25 * 60); // 4h 25m
        }

        loop_now += 24 * 60 * 60 * 1000; // add a day to loop
    }
    return total;
}



function inCalc(start, end, direction) {

    
    var total = timeIntegral(start, end);


    // if day is holiday -> quick return total
    var now = new Date();
    // console.log(now.toISOString().slice(0, 10))
    if (holidays.includes(now.toISOString().slice(0, 10))) {
        console.log("is holiday");
        return total;
    }


    const dayEnd = new Date();

    if (0 < now.getDay() && now.getDay() < 5) {
        dayEnd.setHours(8, 15, 0, 0, 0);
        if (now < dayEnd) {
            return total;
        }

        dayEnd.setHours(12 + 3, 55, 0, 0, 0);

        
        total += (Number(direction) * 2 - 1) * Math.max((dayEnd - now) / 1000.0, 0);

    } else if (now.getDay() === 5) {
        dayEnd.setHours(8, 20, 0, 0, 0);
        if (now < dayEnd) {
            return total;
        }

        dayEnd.setHours(12, 45, 0, 0, 0);
        total += (Number(direction) * 2 - 1) * Math.max((dayEnd - now) / 1000.0, 0);
    }
    //total -= (end of day - now)

    return total;
    // console.log("eeee");
}

// for (let step = 0; step < 5; step++) {}
// const q1In  = inCalc(q1End);

function absCalc(now, end) {
    // var now = new Date( Date.now());
    // console.log(now);

    // 12:45 friday sep 20th 2024

    // document.getElementById('timer').innerHTML = now;
    var diff = (end - now) / 1000;
    // document.getElementById('1seconds').innerHTML = "seconds: " + diff ;
    return diff;

}


function sec2iso(secs) {
    date = new Date(secs * 1000);

    // HMS = date.toISOString().slice(11, 23);
    // days = Math.floor(secs / 86400);
    // part = (days <= 1) ? " Day " : " Days ";
    
    HMS = date.toISOString().slice(11, 23);
    days = Math.floor(secs / 86400);
    // part = (days <= 1) ? " Day: " : " Days: ";
    
    return   days + " +" + HMS;
}

function longFormat(large) {
    return large.toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
}

// until breaks fall, winter, spring, summer
// since summer, fall, winter, spring
// each for in school and abs
// 4 breaks x 2 directions x 2 counting methods
// cant do negitive until passed, so only 5 x 2

const bar=document.getElementById("myBar");

function update() {
    now = new Date();
    // document.getElementById("header").innerHTML = new Date;
    window.setTimeout(update, document.getElementById("timing").value) // used for dynamic timing
    var first=0;

    for (let step = 0; step < 5; step++) {

        var start = now;
        var stop = ends[step - 1];
        var direction = true;

        if (now.getTime() > starts[step].getTime()) {
            stop = start;
            start = starts[step];
            direction = false;
        }
        // console.log(direction)


        for (let mode = 0; mode < 2; mode++) {
            // console.log(start);

            var alt = "abs";
            if (mode === 0) {
                secs = absCalc(start, stop);
            } 
            else if (mode === 1) {
                alt = "in";
                secs = inCalc(start, stop, direction);
                // should be pre calculated on start up
                // subtract the remainder of the day
            }
            // document.getElementById("header").innerHTML = secs;

            // document.getElementById(alt + step + 'seconds').innerHTML =
            //     "seconds: " + secs.toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
            if (step===0 && mode===1 ){
                first=secs;
            }
            document.getElementById(alt + step + 'Seconds').innerHTML =
                // "Seconds: " + longFormat(secs);
                longFormat(secs);
            
            document.getElementById(alt + step + 'Minutes').innerHTML = 
                longFormat(secs/60);

            
            // document.getElementById(alt + step + 'Hours -b').innerHTML = 
            //     "Hours: " + longFormat(secs/60/60);
            document.getElementById(alt + step + 'Hours').innerHTML = 
                longFormat(secs/60/60);

            document.getElementById(alt + step + 'days').innerHTML = 
                sec2iso(secs); 

            document.getElementById(alt + step + 'Weeks').innerHTML =
                longFormat(secs/60/60/24/7);

            document.getElementById(alt + step + 'FortNights').innerHTML =
                longFormat(secs/60/60/24/7/2);
            
            document.getElementById(alt + step + 'hotdogs').innerHTML =
                // "<br>hotdogs eatable by Joey Chestnut: " + longFormat(secs/60/  10*62 );
                longFormat(secs/60/  10*62 );

            document.getElementById(alt + step + 'snail-miles').innerHTML =
                // "<br>snail-miles: " + longFormat(secs/60/60*0.03);
                longFormat(secs/60/60*0.03);


            var lightInch = (secs * (299_792_458 * 39.3700787402)).toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$&,').slice(0,-2);
            // if (lightInch.length > 11){
            //     lightInch= "<br>" + lightInch;
            // }
            
            document.getElementById(alt + step + 'light-inches').innerHTML =
                // "light-inches: " + longFormat(secs * 299_792_458 * 39.3700787402);
                // "light-inches: <br>" +  lightInch.slice(0,-2);
                lightInch;
            

            document.getElementById(alt + step + 'bluey episodes').innerHTML =
                // "<br>bluey episodes: <br>" + longFormat(secs /(6*60+20)   );
                longFormat(secs /(6*60+20)   );

            var eon=(secs/60.0/60/24/365.242374/1_000_000_000).toFixed(33).replace(/\B(?=(\d{3})+(?!\d))/g, " ");
            document.getElementById(alt + step + 'eons').innerHTML =
                // "eons: " + (secs/60/60/24/365.242374/1_000_000_000).toFixed(100-16).replace(/\B(?=(\d{3})+(?!\d))/g, ",")+"," ;
                // "<br>eons: " + eon.slice(0,14) + "<br>" + eon.slice(14,34) ;
                eon.slice(0,14) + "<br>" + eon.slice(14,30);

            
            // elements = document.getElementById("timer").children
            // elements.item(step)
            
            // document.getElementById(names[step]).style.width = (step/5 )* 100 + "%";
            
            if (mode===1 && step===4){ // only on the last itteration
                var percent=Math.min(  (first/(first+secs)*100).toFixed(6),100   ) + "%";
                document.getElementById('percent').innerHTML = percent;
                // console.log(mode,percent,first+secs);
                bar.style.width = percent;
            }
            
            if (0<step && step<5) {
                // secs #2 needs to be the last time
                document.getElementById(step).style.width = (first+secs)/(4_534_200)*100-.8+"%"; 
                //24908700 is total seconds in the school year //3_970_000
                // if (mode===1){
                //     console.log(mode,step,(first+secs)/(4_534_200)*100+"%")
                // }
            }
        }
    }    
}


function detectMob() {
    const toMatch = [
        /Android/i,
        /webOS/i,
        /iPhone/i,
        /iPad/i,
        /iPod/i,
        /BlackBerry/i,
        /Windows Phone/i
    ];

    return toMatch.some((toMatchItem) => {
        return navigator.userAgent.match(toMatchItem);
    });

}

// const pc = true;
const pc = !detectMob();

const units=[
    "Seconds -b",
    "Minutes -b",
    "Hours -b",
    "days -b",
    "Weeks -b",
    "FortNights -b",
    "eons -b -l",
    "snail-miles -b -l",
    "light-inches -a",
    "hotdogs -b",
    "bluey episodes -a",
    
    
];

function unitP(abs, step){
    var output = "";
    for (let unit of units) { 
        // <sup><a id="ftn-1-ref" href="#ftn-1">[1]</a></sup>
        // if (unit.includes("-1") or unit.includes("-2")){
        //     output+="<br>";
        //     unit=unit.slice(0,-3);
        // }
        // const regex = /-(\d+)$/;
        // const match = str.match(regex);
        
        
        if (unit.includes("-l")){
            output+="<br>";
            unit=unit.slice(0,-3);
        }
            
        if (unit.includes("-b")){
            output+= ` <p style = "display: flex; justify-content: space-between;">
                            <span style= "white-space:pre;">${unit.slice(0,-3)}: </span>
                            <span id="${abs}${step}${unit.slice(0,-3)}"  style="text-align:right; " > </span> 
                        </p>`;

        } else if(unit.includes("-a")){
            output+= `<p style="width:100%;">
                        <span style= "display: inline-block;white-space: nowrap;">${unit.slice(0,-3)}: </span>
                        
                      </p>
                      <span id="${abs}${step}${unit.slice(0,-3)}"  style="display: inline-block; white-space: nowrap; text-align:right; float:right;" > </span> 
                      <br><br>
                      `;
        } else {
           output+= `<p id="${abs}${step}${unit}">it's bwokin ;(</p>`;//) 
        }
        
    } 
    
    return output;
} 
const timer = document.getElementById("timer")

// summer, fall, winter, spring, and summer change depending on before/after
for (let step = 0; step < 5; step++) {
    var label = "Until " + names[step];
    // console.log(now.getTime() ,starts[step].getTime())

    if (now.getTime() > starts[step].getTime()) {
        label = "Since " + names[step];
        
    }
    var style = "";
    if (pc) {
        style = ' style = "flex: 1 1 10%; margin: .2vw; justify-content: space-around;" ';
    }

    // document.getElementById(names[step]).style.width = (step/5 )* 100 + "%";
    // document.getElementById(names[step]).style.width = step/4*100+"%";

    
    // document.getElementById("timer").innerHTML += `
    timer.innerHTML += `

    <details class="docio_output" id="base${step}" open${style}>
        <summary>
        Time ${label} Break
        </summary>
        <div id="abs${step}" style="display:revert;" >
            <h3>Absolute Time</h3>
            ${unitP("abs",step)}
        </div>
        <div id="in${step}"   style="display:revert;">
            <h3>In School Time</h3>
            ${unitP("in",step)}
        </div>
    </details>
    `;
///style="display: inline-block;"
// <p id="abs${step}formated">it's bwokin ;(</p>>)
//             <p id="abs${step}seconds">it's bwokin ;(</p>)
//             <p id="abs${step}minutes">it's bwokin ;(</p>)
//             <p id="abs${step}hours">it's bwokin ;(</p>)


} 

if (pc) {
    // document.getElementById("timer").style.display = "flex";
    // document.getElementById("timer").style.flexWrap = "wrap";    
    timer.style.display = "flex";
    timer.style.flexWrap = "wrap";
    //display: flex;
    //flex-wrap: wrap;
}

// var timing = document.getElementById("timing");
// setInterval(update, 33); 
// 33 milliseconds -> 30 frames per sec 
// or 16.6 mili -> 60 fps 
// or 13.3 mili -> 75 fps

const contextMenu = document.getElementById('contextMenu');
const checklist = document.getElementById('checks');

document.body.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    contextMenu.style.display = 'block';
    contextMenu.style.left = `${e.pageX}px`;
    contextMenu.style.top = `${e.pageY}px`;

    for ( let i=0; i<5;i++){

        // console.log(i,checklist.children[i],timer.children[i],timer.children[i].open)
        // console.dir(checklist.children[i].firstElementChild.firstElementChild)
        // console.log(checklist.children[i].firstElementChild.firstElementChild.checked)
        checklist.children[i].firstElementChild.firstElementChild.checked = timer.children[i].open;
        // checklist.children[i].firstElementChild.firstElementChild.checked = false;
    }


    
}); // show

document.addEventListener('click', function () {
    contextMenu.style.display = 'none';
}); // hide


checklist.addEventListener('click', function (e) {
            
    const checkbox = e.target;
    const column = checkbox.getAttribute('data-column');
    const isChecked = checkbox.checked;
    console.log(column);
    if (column === null){
      return 0;
    }
    // console.log(timer.children);
    // console.log(timer.children[column]);
    // console.dir(timer.children[column]);  
    
    timer.children[column].open = !timer.children[column].open;
    // timer.children[column].removeAttribute('open');
    
    // const headers = table.querySelectorAll(`thead th:nth-child(${parseInt(column)+1})`);
    // const cells   = table.querySelectorAll(`tbody td:nth-child(${parseInt(column)+1})`);

    // headers.forEach(header => {header.style.display=isChecked ? '':'none'});
    // cells.forEach(cell => {cell.style.display=isChecked ? '':'none'});
});

        

update();



