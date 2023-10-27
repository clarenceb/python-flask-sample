// Generate code below using GitHub Copilot.
// K6 script to hit endpoint https://helloazureflask.azurewebsites.net/ for 30s with 10 VUs

import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
    vus: 10,
    duration: '30s',
    };

export default function () {
    http.get('https://helloazureflask.azurewebsites.net/');
    sleep(0.1);
    }
