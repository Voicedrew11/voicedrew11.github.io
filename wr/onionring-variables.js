// onionring.js is made up of four files - onionring-widget.js, onionring-index.js, onionring-variables.js (this one!), and onionring.css
// it's licensed under the cooperative non-violent license (CNPL) v4+ (https://thufie.lain.haus/NPL.html)
// it was originally made by joey + mord of allium (蒜) house, last updated 2020-11-24

// === ONIONRING-VARIABLES ===
//this file contains the stuff you edit to set up your specific webring

//the full URLs of all the sites in the ring
var sites = [
'https://forum.agoraroad.com/index.php',
'https://voicedrew.xyz/',
'https://myyolo1999.blogspot.com/p/ja.html',
'https://i330.dev',
'https://idelides.xyz/',
'https://risingthumb.xyz/',
'https://foreverliketh.is/',
'https://whitevhs.xyz/',
'https://h00.neocities.org/',
'https://www.zeropointfool.com/',
'https://tilde.team/~zinricky/',
'https://sizeof.cat/',
'https://aralsheart.ichi.city/',
'https://wkyk.neocities.org/',
'https://walrus-island.neocities.org/',
'https://freckleskies.neocities.org/',
'https://microbyte.neocities.org/',
'https://dorgon.neocities.org/',
'https://andrei.xyz/',
'https://insomniac.ichi.city/',
'https://nhkhq.neocities.org/',
'https://starbreaker.org/',
'https://aboboracandy.neocities.org/',
'https://blog.shr4pnel.com',
'https://skeleg.org',
'https://no56.neocities.org/',
'https://yuiui.moe/',
'https://digitalcheese.xyz/',
'https://splashy.neocities.org/',
'https://purplehello98.neocities.org/',
'https://vulonkaaz.zip/',
'https://genosadness.neocities.org/',
'https://kodeb8.neocities.org/',
'https://www.scitzoe.com/',
'https://b4rkod.net.tr/',
'https://psychcool.neocities.org/',
'https://georgemoody.envs.net/',
'https://chrysalism.neocities.org/',
'https://crunglechamp.neocities.org/',
'https://alixx.ichi.city/',
'https://omnipresence.neocities.org/',
'https://hwii.net/',
];

// 'https://nhkcafe.neocities.org/',

//the name of the ring
var ringName = 'Travelers of Agora Road';

/* the unique ID of the widget. two things to note:
 1) make sure there are no spaces in it - use dashes or underscores if you must
 2) remember to change 'webringid' in the widget code you give out and all instances of '#webringid' in the css file to match this value!*/
var ringID = 'tag-webring';

//should the widget include a link to an index page?
var useIndex = true;
//the full URL of the index page. if you're not using one, you don't have to specify anything here
var indexPage = 'https://voicedrew.xyz/wr/';

//should the widget include a random button?
var useRandom = true;
