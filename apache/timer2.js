var now = new Date(Date.now());

var start = new Date(2025, 7-1, 16, 8, 15)
var end = new Date(2026, 5-1, 22, 12, 45)


//holidays & breaks
//sep 1
//sep 22-26
//nov 24-28
//dec 22-31
//jan 1-5
//jan 19
//feb 16
//mar 9-23
//apr 3

// List holidays/breaks as arrays of [startDate, endDate] (inclusive)
const holidays = [
    [new Date(2023, 8-1, 1), new Date(2023, 8-1, 1)], // Sep 1
    [new Date(2023, 8-1, 22), new Date(2023, 8-1, 26)], // Sep 22-26
    [new Date(2023, 11-1, 24), new Date(2023, 11-1, 28)], // Nov 24-28
    [new Date(2023, 12-1, 22), new Date(2023, 12-1, 31)], // Dec 22-31
    [new Date(2024, 1-1, 1), new Date(2024, 1-1, 5)], // Jan 1-5
    [new Date(2024, 1-1, 19), new Date(2024, 1-1, 19)], // Jan 19
    [new Date(2024, 2-1, 16), new Date(2024, 2-1, 16)], // Feb 16
    [new Date(2024, 3-1, 9), new Date(2024, 3-1, 23)], // Mar 9-23
    [new Date(2024, 4-1, 3), new Date(2024, 4-1, 3)], // Apr 3
];

// Helper to check if a date is in a holiday
function isHoliday(date) {
    for (const [start, end] of holidays) {
        if (date >= start && date <= end) return true;
    }
    return false;
}

// Returns seconds of school time between now and end
function getSchoolSeconds(now, end) {
    let totalSeconds = 0;
    let current = new Date(now);
    

    while (current < end) {
        // Skip weekends
        const day = current.getDay();
        if (day === 0 || day === 6) { // Sunday or Saturday
            current.setDate(current.getDate() + 1);
            current.setHours(0,0,0,0);
            continue;
        }
        // Skip holidays
        if (isHoliday(current)) {
            current.setDate(current.getDate() + 1);
            current.setHours(0,0,0,0);
            continue;
        }

        let schoolStart, schoolEnd;
        if (day === 5) { // Friday
            schoolStart = new Date(current.getFullYear(), current.getMonth(), current.getDate(), 8, 20, 0, 0);
            schoolEnd = new Date(current.getFullYear(), current.getMonth(), current.getDate(), 12, 45, 0, 0);
        } else { // Mon-Thu
            schoolStart = new Date(current.getFullYear(), current.getMonth(), current.getDate(), 8, 15, 0, 0);
            schoolEnd = new Date(current.getFullYear(), current.getMonth(), current.getDate(), 15, 55, 0, 0);
        }

        // If current date is today, adjust start
        let from = current > schoolStart ? current : schoolStart;
        let to = end < schoolEnd ? end : schoolEnd;

        if (from < to) {
            totalSeconds += (to - from) / 1000;
        }

        // Move to next day
        current.setDate(current.getDate() + 1);
        current.setHours(0,0,0,0);
    }
    return totalSeconds;
}



const bar=document.getElementById("myBar");

const timer = document.getElementById("timer")

const units=[
    "Seconds -b",
    "Minutes -b",
    "Hours -b",
    "Days -b",
    "Weeks -b",
    "FortNights -b",
    "Moons -b",
    "years -b -l",
    // "decades -b -l",
    // "centuries -b -l",
    // "millennia -b -l",
    // "megaanna -b -l",
    "Eons -b -l",
    "snail-miles -s -l",
    "light-inches -b",
    "Hotdogs -h",
    "Bluey episodes -b",
    "inflation -a"
    
];


/// setup
function unitP(abs, step){
    var output = "";
    i=0;
    for (let unit of units) { 
        // <sup><a id="ftn-1-ref" href="#ftn-1">[1]</a></sup>
        // if (unit.includes("-1") or unit.includes("-2")){
        //     output+="<br>";
        //     unit=unit.slice(0,-3);
        // }
        // const regex = /-(\d+)$/;
        // const match = str.match(regex);
        
        if (unit.includes("-l")){
            // output+="<br>";
            unit=unit.slice(0,-3);
        }
        
            
        // Determine background color based on i
        const bgStyle = (i % 2 === 0) ? 'background-color: #585858;' : '';

        if (unit.includes("-b")){
            output+= ` <p style="display: flex; justify-content: space-between; ${bgStyle}">
                    <span style="white-space:pre;">${unit.slice(0,-3)}: </span>
                    <span id="${abs}${step}${unit.slice(0,-3)}" style="text-align:right;"> </span> 
                </p>`;
        } else if(unit.includes("-a")){
            output+= `<p style="width:100%; ${bgStyle}">
                <span style="display: inline-block;white-space: nowrap;">${unit.slice(0,-3)}: </span>
                  </p>
                  <span id="${abs}${step}${unit.slice(0,-3)}" style="display: inline-block; white-space: nowrap; text-align:right; float:right;"> </span>`;
        } else if (unit.includes("-h")){
            output+= ` <p style="display: flex; justify-content: space-between; ${bgStyle}">
                    <span style="white-space:pre;">${unit.slice(0,-3)}<sup><a href="#5">5</a></sup>: </span>
                    <span id="${abs}${step}${unit.slice(0,-3)}" style="text-align:right;"> </span> 
                </p>`;
        } else if (unit.includes("-s")){
            output+= ` <p style="display: flex; justify-content: space-between; ${bgStyle}">
                    <span style="white-space:pre;">${unit.slice(0,-3)}<sup><a href="https://www.youtube.com/watch?v=m7D8ilwnUzk">4</a></sup>: </span>
                    <span id="${abs}${step}${unit.slice(0,-3)}" style="text-align:right;"> </span> 
                </p>`;
        } else {
           output+= `<p id="${abs}${step}${unit}" style="${bgStyle}">it's bwokin ;(</p>`;
        }

        i++;

    }

    return output;
} 


timer.innerHTML = `
    <details class="docio_output" id="base${1}" open>
        <summary>
        End of School
        </summary>

        <div id="abs${1}" style="display:revert;" >
            <h3>Absolute Time</h3>
            ${unitP("abs",1)}
        </div>

        <div id="in${1}"   style="display:revert;">
            <h3>In School Time</h3>
            ${unitP("in",1)}
        </div>

        <div id="data"   style="display:revert;">
            <h3>data science</h3>
            <p style="display: flex; justify-content: space-between;">
                <span style="white-space:pre;">ratio</sup>: </span>
                <span id="ratio" style="text-align:right;"> </span> 
            </p>
        </div>

    </details>
`




function formatEonsWithSpaces(value,places=9) {
    let str = value.toFixed(places);
    let [intPart, fracPart] = str.split('.');
    if (fracPart) {
        fracPart = fracPart.replace(/(\d{3})(?=\d)/g, '$1 ');
        return intPart + '.' + fracPart;
    }
    return intPart;
}


function formatCountdown(totalSeconds) {
    if (!isFinite(totalSeconds) || totalSeconds < 0) totalSeconds = 0;

    const NBSP = '\u00A0';

    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = Math.floor(totalSeconds % 60);
    const ms = Math.floor((totalSeconds * 1000) % 1000);

    const showHours = hours > 0;
    const showMinutes = showHours || minutes > 0;
    const showSeconds = showMinutes || seconds > 0;

    // Show ms if seconds are shown (to display ".000") OR there are non-zero milliseconds
    const showMs = showSeconds || ms > 0;

    const leftmost = showHours ? 'hours' : (showMinutes ? 'minutes' : (showSeconds ? 'seconds' : null));

    function field(val, width, name) {
        if ((name === 'hours' && !showHours) || (name === 'minutes' && !showMinutes) || (name === 'seconds' && !showSeconds)) {
            return NBSP.repeat(width);
        }
        const padChar = (leftmost === name) ? NBSP : '0';
        return String(val).padStart(width, padChar);
    }

    const hStr = field(hours, 4, 'hours');
    const mStr = field(minutes, 2, 'minutes');
    const sStr = field(seconds, 2, 'seconds');

    // ms: when visible pad with '0' so we show "000" for exact seconds; otherwise preserve width with NBSPs
    const msStr = showMs ? String(ms).padStart(3, '0') : NBSP.repeat(3);

    const hasDigit = str => /\d/.test(str);

    // invisible separators use a zero-opacity span so layout/width is preserved
    const invisibleColon = '<span style="opacity:0">:</span>';
    const invisibleDot = '<span style="opacity:0">.</span>';

    // show a separator only if there are digits on both sides (hides when higher value is absent)
    const sepHM = (hasDigit(hStr) && hasDigit(mStr)) ? ':' : invisibleColon;
    const sepMS = (hasDigit(mStr) && hasDigit(sStr)) ? ':' : invisibleColon;

    // show dot whenever ms are actually shown
    const dot = hasDigit(msStr) ? '.' : invisibleDot;

    return `${hStr}${sepHM}${mStr}${sepMS}${sStr}${dot}${msStr}`;
}

function update() {
    now = new Date();
    // now = new Date(2026,4,21,10,30);
    window.setTimeout(update, document.getElementById("timing").value);

    var diff = (end - now) / 1000;
    var inDiff = getSchoolSeconds(now, end);

    // Absolute time
    document.getElementById("abs" + 1 + 'Seconds'       ).innerHTML =  diff                     .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("abs" + 1 + 'Minutes'       ).innerHTML = (diff/60)                 .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("abs" + 1 + 'Hours'         ).innerHTML = (diff/60/60)              .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("abs" + 1 + 'Days'          ).innerHTML = (diff/60/60/24)           .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("abs" + 1 + 'Weeks'         ).innerHTML = (diff/60/60/24/7)         .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("abs" + 1 + 'FortNights'    ).innerHTML = (diff/60/60/24/7/2)       .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("abs" + 1 + 'Moons'         ).innerHTML = (diff/60/60/24/29.53)     .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    
    document.getElementById("abs" + 1 + 'years'         ).innerHTML = formatEonsWithSpaces(diff/60/60/24/365.2425               ,9);
    // document.getElementById("abs" + 1 + 'decades'       ).innerHTML = formatEonsWithSpaces(diff/60/60/24/365.2425/10            ,9);
    // document.getElementById("abs" + 1 + 'centuries'     ).innerHTML = formatEonsWithSpaces(diff/60/60/24/365.2425/100           ,9);
    // document.getElementById("abs" + 1 + 'millennia'     ).innerHTML = formatEonsWithSpaces(diff/60/60/24/365.2425/1_000         ,9);
    // document.getElementById("abs" + 1 + 'megaanna'      ).innerHTML = formatEonsWithSpaces(diff/60/60/24/365.2425/1_000_000     ,9);
    document.getElementById("abs" + 1 + 'Eons'          ).innerHTML = formatEonsWithSpaces(diff/60/60/24/365.2425/1_000_000_000 ,18);
    
    document.getElementById("abs" + 1 + 'snail-miles'   ).innerHTML = formatEonsWithSpaces(diff/60/60*0.03,6);
    document.getElementById("abs" + 1 + 'light-inches'  ).innerHTML = (diff*299_792_458*39.370_078_740_2)   .toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$&,').slice(0,-2);
    document.getElementById("abs" + 1 + 'Hotdogs'       ).innerHTML = (diff/60/10*76)           .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("abs" + 1 + 'Bluey episodes').innerHTML = (diff/60/7)               .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');


    // In School Time
    document.getElementById("in" + 1 + 'Seconds'        ).innerHTML =  inDiff                   .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("in" + 1 + 'Minutes'        ).innerHTML = (inDiff/60)               .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("in" + 1 + 'Hours'          ).innerHTML = (inDiff/60/60)            .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("in" + 1 + 'Days'           ).innerHTML = (inDiff/60/60/24)         .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("in" + 1 + 'Weeks'          ).innerHTML = (inDiff/60/60/24/7)       .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("in" + 1 + 'FortNights'     ).innerHTML = (inDiff/60/60/24/7/2)     .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("in" + 1 + 'Moons'          ).innerHTML = (inDiff/60/60/24/29.53)   .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    
    document.getElementById("in" + 1 + 'years'          ).innerHTML = formatEonsWithSpaces(inDiff/60/60/24/365.2425                 ,9);
    // document.getElementById("in" + 1 + 'decades'        ).innerHTML = formatEonsWithSpaces(inDiff/60/60/24/365.2425/10              ,9);
    // document.getElementById("in" + 1 + 'centuries'      ).innerHTML = formatEonsWithSpaces(inDiff/60/60/24/365.2425/100             ,9);
    // document.getElementById("in" + 1 + 'millennia'      ).innerHTML = formatEonsWithSpaces(inDiff/60/60/24/365.2425/1_000           ,9);
    // document.getElementById("in" + 1 + 'megaanna'       ).innerHTML = formatEonsWithSpaces(inDiff/60/60/24/365.2425/1_000_000       ,9);
    document.getElementById("in" + 1 + 'Eons'           ).innerHTML = formatEonsWithSpaces(inDiff/60/60/24/365.2425/1_000_000_000   ,18);
    
    document.getElementById("in" + 1 + 'snail-miles'    ).innerHTML = formatEonsWithSpaces(inDiff/60/60*0.03,6);
    document.getElementById("in" + 1 + 'light-inches'   ).innerHTML = (inDiff*299_792_458*39.370_078_740_2) .toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$&,').slice(0,-2);
    document.getElementById("in" + 1 + 'Hotdogs'        ).innerHTML = (inDiff/60/10*76)         .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById("in" + 1 + 'Bluey episodes' ).innerHTML = (inDiff/60/7)             .toFixed(3).replace(/\d(?=(\d{3})+\.)/g, '$&,');

    //data science
    document.getElementById("ratio").innerHTML = ((diff/inDiff)*100).toFixed(6).replace(/\d(?=(\d{3})+\.)/g, '$&,') + "%";

    // mixed number countdown
    // inDiff -= 3600 * 1069 ; // testing
    // inDiff -= 60 * 14 ;
    // inDiff = 0.000;
    // inDiff -= 3839750; // to test zero countdown
    // inDiff %=100; // 
    // inDiff /=100;
    mixed= 
        Math.floor(inDiff/60/60) +
        ":" +
        String(Math.floor((inDiff/60)%60)).padStart(2,'0') +
        ":" +
        String(Math.floor(inDiff%60)).padStart(2,'0') +
        "." +
        String(Math.floor((inDiff*1000)%1000)).padStart(3,'0');
    
    mixed = formatCountdown(inDiff);

    // When the in-school countdown has hit zero, show "0000:00:00.000" and make it flash.
    const mixedEl = document.getElementById("mixed");
    const mixed2El = document.getElementById("mixed2");
    if (inDiff <= 0) {
        mixed = "0000:00:00.000";
        if (mixedEl) mixedEl.classList.add("flash");
        if (mixed2El) mixed2El.classList.add("flash");
    } else {
        if (mixedEl) mixedEl.classList.remove("flash");
        if (mixed2El) mixed2El.classList.remove("flash");
    }

    document.getElementById("mixed").innerHTML = mixed;
    document.getElementById("mixed2").innerHTML = mixed;

    // ghost-eights: mirror digits as 8 but preserve &nbsp; and punctuation
    // document.getElementById("ghost-eights").innerHTML = mixed.replace(/\d/g, '8');
    
}
// update()

