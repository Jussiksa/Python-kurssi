'use strict';
const name = prompt('Enter student name:');
const draw = Math.floor(Math.random() *4) + 1;
let house = '';

switch (draw)  {
    case 1:
        house    = 'Gryffindor';
        break;
        case 2:
            house = 
            'Slytherin';
            break;
            case 3:
                house = 'Huffelpff';
                break;
                case 4:
                    house = 'Ravenclaw';
                    break;
}
document.querySelector('#target').textContent =name + ', you are ' + house + '.';

    