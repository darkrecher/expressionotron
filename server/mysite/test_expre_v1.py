# Pour lancer les tests, il faut exécuter dans la console :
# python -m py.test
# Si on fait "py.test" tout seul ça ne marche pas.
# (sûrement pour la même raison qu'il faut faire "python -m pip install truc",
# sûrement parce que je suis sous Windows.)

from expressionotron.v001.expr_generator import generate_expression


def test_generate_expression_v001_one():
    assert generate_expression(0) == "&Ccedil;a desquame du doppelganger crypto-bisexuel au Spero Patronum !! 11! !!1"


def test_generate_expression_v001_many():

    TEST_DATA = (
        ("&Ccedil;a tron&ccedil;onne du chaton en armure de plates &agrave; la Holy Grenade !! 11! !!1", 140997840),
        ("&Ccedil;a merge du creep franco-psychopathe au moule &agrave; gauffre !! 11! !!1", 117139760),
        ("&Ccedil;a vampirise du clapatte endo-gobelettoforme &agrave; la cyprine !! 11! !!1", 280050428),
        ("&Ccedil;a poutre du professeur d'anglais bugg&eacute; &agrave; coups de pain tueur !! 11! !!1", 196262884),
        ("&Ccedil;a snipe du brontosaure triclass&eacute; en buzzant &agrave; donf !! 11! !!1", 153489573),
        ("&Ccedil;a mine du korrigans version shareware &agrave; la massue en mousse !! 11! !!1", 247959298),
        ("&Ccedil;a d&eacute;soxyribe du raptor s&eacute;v&eacute;rement burn&eacute; &agrave; la grenade antichar !! 11! !!1", 210451200),
        ("&Ccedil;a d&eacute;soxyribe du gnome lvl 99 au gaz &agrave; effets de serre !! 11! !!1", 102106788),
        ("&Ccedil;a caniculise de l'extrad&eacute; bouddhiste &agrave; la grenade antichar !! 11! !!1", 43732751),
        ("&Ccedil;a d&eacute;pr&eacute;cate du g&eacute;niteur de deuxi&egrave;me g&eacute;n&eacute;ration &agrave; coups d'extincteur !! 11! !!1", 203564318),
        ("&Ccedil;a coup-critique du mouflon crapuleux au gaz &agrave; effets de serre !! 11! !!1", 18269322),
        ("&Ccedil;a saponifie du lolcat pre-narquois comme dans du beurre !! 11! !!1", 137834587),
        ("&Ccedil;a poutre du Yoshi philat&eacute;liste au pays des merveilles !! 11! !!1", 191605708),
        ("&Ccedil;a plaque-techtonise du romanichel ind&eacute;pendantiste &agrave; la vol&eacute;e !! 11! !!1", 22765221),
        ("&Ccedil;a bankablise du golem de p&acirc;t&eacute; sous acide au Baygon !! 11! !!1", 285029174),
        ("&Ccedil;a tsunamise du kilmoulis am&eacute;ricano-sid&eacute;ral au choux de bruxelles !! 11! !!1", 216847880),
        ("&Ccedil;a pollinise de l'iTruc version beta &agrave; la mitrailleuse g&eacute;ante de Counter-Strike !! 11! !!1", 89681958),
        ("&Ccedil;a dissout du smiley nymphomane &agrave; la vol&eacute;e !! 11! !!1", 94409035),
        ("&Ccedil;a merge du clapatte ultra-clignotant avec du caca !! 11! !!1", 22582520),
        ("&Ccedil;a &eacute;chec-critique de l'Eric Cartmann mucoviscideux au forceps !! 11! !!1", 290818987),
        ("&Ccedil;a caniculise du rongeur journalistique au willy waller !! 11! !!1", 69719927),
        ("&Ccedil;a alcoolise de l'extrad&eacute; interop&eacute;rable en chantant une chanson paillarde !! 11! !!1", 31961770),
        ("&Ccedil;a head-shote du gretchin mega-v&eacute;reux &agrave; la mitrailleuse g&eacute;ante de Counter-Strike !! 11! !!1", 142002478),
        ("&Ccedil;a d&eacute;sint&egrave;gre du kilmoulis racaillou au frottis vaginal !! 11! !!1", 131282280),
        ("&Ccedil;a canonise du vagin de truie catho-clignotant &agrave; coups de petits cailloux dans les yeux !! 11! !!1", 236315958),
        ("&Ccedil;a poutre du gnome cubistes au fer &agrave; friser !! 11! !!1", 27908488),
        ("&Ccedil;a canonise de l'andouille extra-pestif&eacute;r&eacute; &agrave; la kqlqsh !! 11! !!1", 138055506),
        ("&Ccedil;a sacque du hamster du zodiaque comme Marion Cotillard !! 11! !!1", 237615464),
        ("&Ccedil;a g&eacute;nocide de la prostate m&eacute;cano-fukushimien au sabre laser !! 11! !!1", 60168836),
        ("&Ccedil;a charcle du smiley guerrier-mage-clerc en mode nightmare !! 11! !!1", 20907615),
        ("&Ccedil;a d&eacute;sacralise du clapatte iconoclaste &agrave; la lame vorpale !! 11! !!1", 112650871),
        ("&Ccedil;a &eacute;chec-critique du hamster juda&iuml;stico-frigide avec du caca !! 11! !!1", 14714935),
        ("&Ccedil;a choc-m&eacute;tabolise du papillon de lumi&egrave;re anticonstitutionnel comme dans un film de John Woo !! 11! !!1", 294463165),
        ("&Ccedil;a mondialise de l'andouille m&eacute;trique aux impulsions &eacute;lectro-magn&eacute;tiques !! 11! !!1", 85386453),
        ("&Ccedil;a trucide de l'australopith&egrave;que n&eacute;o-abracadabrantesque au moule &agrave; gauffre !! 11! !!1", 47971344),
        ("&Ccedil;a jail-break du roflcopter contractuel &agrave; la grenade antichar !! 11! !!1", 27330971),
        ("&Ccedil;a dissout du ninja giga-m&eacute;trique aux impulsions &eacute;lectro-magn&eacute;tiques !! 11! !!1", 135070495),
        ("&Ccedil;a cocufie du zombi grand-guignolesque au BFG !! 11! !!1", 52117872),
        ("&Ccedil;a pl&acirc;tre du smiley version beta aux impulsions &eacute;lectro-magn&eacute;tiques !! 11! !!1", 190614540),
        ("&Ccedil;a desquame de l'Utu ultra-tentaculaire &agrave; la cyprine !! 11! !!1", 146569824),
        ("&Ccedil;a d&eacute;moule du schtroumpf volumique au karcher !! 11! !!1", 263344065),
        ("&Ccedil;a synchrotronne du secr&eacute;taire g&eacute;n&eacute;ral UMP m&eacute;cano-tentaculaire au gravier-cailloux-gros sel !! 11! !!1", 188415306),
        ("&Ccedil;a head-shote du dictateur du 16&egrave;me si&egrave;cle comme dans un vieux rock'n'roll !! 11! !!1", 43619662),
        ("&Ccedil;a viande du pirate fant&ocirc;me sur-bisexuel avec de l'hydrog&egrave;ne et du temps !! 11! !!1", 238980655),
        ("&Ccedil;a jail-break du zergling callifragilistique comme dans un vieux rock'n'roll !! 11! !!1", 259874519),
        ("&Ccedil;a pistouille du professeur d'anglais du zodiaque &agrave; coups de petits cailloux dans les yeux !! 11! !!1", 198653295),
        ("&Ccedil;a d&eacute;gobille du trilobyte hexakosioihexekontahexaphobe &agrave; la Holy Grenade !! 11! !!1", 218718670),
        ("&Ccedil;a l&eacute;galise du raptor issu de la diversit&eacute; au willy waller !! 11! !!1", 114047598),
        ("&Ccedil;a poutre du roflcopter texan &agrave; la massue en mousse !! 11! !!1", 235270324),
        ("&Ccedil;a &eacute;clabousse de l'Utu racaillou au RPG !! 11! !!1", 125689067),
        ("&Ccedil;a g&eacute;nocide du v&eacute;lociraptor contre nature en buzzant &agrave; donf !! 11! !!1", 26478413),
        ("&Ccedil;a vitrifie du secr&eacute;taire d'&eacute;tat sid&eacute;ral au cocktail molotov !! 11! !!1", 288041411),
        ("&Ccedil;a d&eacute;culotte du tib&eacute;tain macro-batave &agrave; la disquette 3 pouces et demi !! 11! !!1", 121179075),
        ("&Ccedil;a fraise du golden retriever cyber-branquignol au cheval de Troie !! 11! !!1", 126399596),
        ("&Ccedil;a porcherise du p&eacute;gase rouge et jaune &agrave; petit pois avec des hashtags litigieux !! 11! !!1", 31969178),
        ("&Ccedil;a t&eacute;l&eacute;kin&eacute;site du vagin de truie moldave on the rocks !! 11! !!1", 31831533),
        ("&Ccedil;a &eacute;chec-critique du hamster musulman au pied de biche !! 11! !!1", 39047551),
        ("&Ccedil;a d&eacute;pouille du PDG hydroc&eacute;phale avec un balai &agrave; chiottes !! 11! !!1", 79320569),
        ("&Ccedil;a destructure du creep s&eacute;v&eacute;rement burn&eacute; au Decap four !! 11! !!1", 240534037),
        ("&Ccedil;a porcherise de l'octog&eacute;naire hermaphrodite au Famas !! 11! !!1", 32891282),
        ("&Ccedil;a destructure de l'humoriste unijambiste au cheval de Troie !! 11! !!1", 29157623),
        ("&Ccedil;a canonise du Corbier baroque sans les mains !! 11! !!1", 172865742),
        ("&Ccedil;a troue de l'iTruc catholique au railgun !! 11! !!1", 220488076),
        ("&Ccedil;a vilipende du Michel Drucker rose caca d'oie &agrave; la lame vorpale !! 11! !!1", 200512070),
        ("&Ccedil;a d&eacute;chire du commercial boulettesque au sho-ryu-ken !! 11! !!1", 5824016),
        ("&Ccedil;a sodomise facialement de la licorne m&eacute;trique aux impulsions &eacute;lectro-magn&eacute;tiques !! 11! !!1", 142795857),
        ("&Ccedil;a d&eacute;plombe du sbire gr&eacute;vistes sans les mains !! 11! !!1", 17254062),
        ("&Ccedil;a zlatane du vulcain ex-pestif&eacute;r&eacute; au pays des merveilles !! 11! !!1", 71682034),
        ("&Ccedil;a head-shote du caniche de combat cryog&eacute;nis&eacute; avec emphase !! 11! !!1", 293199130),
        ("&Ccedil;a lamine du commercial ultra-humide &agrave; la Holy Grenade !! 11! !!1", 72107127),
        ("&Ccedil;a caresse du pingouin Linux disproportionn&eacute; &agrave; la r&acirc;pe &agrave; fromage !! 11! !!1", 169686921),
        ("&Ccedil;a viande du vagin de truie disproportionn&eacute; au sho-ryu-ken !! 11! !!1", 46773163),
        ("&Ccedil;a mondialise de l'octog&eacute;naire frigide au willy waller !! 11! !!1", 213148833),
        ("&Ccedil;a destructure du paladin journalistique &agrave; la r&acirc;pe &agrave; fromage !! 11! !!1", 198870337),
        ("&Ccedil;a grattouille de l'Eric Cartmann exo-triclass&eacute; &agrave; coups de Bouda !! 11! !!1", 192230537),
        ("&Ccedil;a merge de l'huguenot lvl 99 avec du Destop !! 11! !!1", 71033588),
        ("&Ccedil;a chattouille du manchot empereur m&eacute;cano-texan &agrave; l'enforcer !! 11! !!1", 75641080),
        ("&Ccedil;a sodomise facialement du t&eacute;tra&egrave;dre post-ploutocrate on the rocks !! 11! !!1", 76120545),
        ("&Ccedil;a d&eacute;pr&eacute;cate de l'humoriste ex-racaillou &agrave; la kqlqsh !! 11! !!1", 189325274),
        ("&Ccedil;a cale&ccedil;onne du roflcopter sur-hexakosioihexekontahexaphobe au Baygon !! 11! !!1", 252454119),
        ("&Ccedil;a lamine du p&eacute;gase-licorne soixante-huitard au papier de verre !! 11! !!1", 274657131),
        ("&Ccedil;a kill-steal du romanichel rutilant avec des traces de pneus !! 11! !!1", 194691724),
        ("&Ccedil;a d&eacute;pote du lolcat musulman &agrave; la chirurgie plastique !! 11! !!1", 256284752),
        ("&Ccedil;a head-shote du tyrannosaure narquois &agrave; la vol&eacute;e !! 11! !!1", 29059210),
        ("&Ccedil;a vilipende du professeur d'anglais catho-g&eacute;latineux dans un h&ocirc;tel borgne !! 11! !!1", 49539842),
        ("&Ccedil;a sublime de l'ewok gr&eacute;vistes au disrupteur dimensionnel !! 11! !!1", 93666842),
        ("&Ccedil;a canonise du chaton fukushimien au Spero Patronum !! 11! !!1", 159082890),
        ("&Ccedil;a bankablise de l'andouille sino-matriarcal au sabre laser !! 11! !!1", 158857526),
        ("&Ccedil;a claque du Corbier hydroc&eacute;phale au fusil blaster !! 11! !!1", 46256935),
        ("&Ccedil;a sublime du zergling silicon&eacute; sans les mains !! 11! !!1", 174168314),
        ("&Ccedil;a l&eacute;galise du mini-boss sardonique &agrave; l'acide chlorhydrique !! 11! !!1", 225774570),
        ("&Ccedil;a mondialise du punk freudien au b&acirc;ton de berger !! 11! !!1", 247700409),
        ("&Ccedil;a &eacute;chec-critique du Tutsi frigide en chantant une chanson paillarde !! 11! !!1", 243972691),
        ("&Ccedil;a dissout du sbire maxi-patato&iuml;dal au c&ocirc;ne de froid !! 11! !!1", 274151923),
        ("&Ccedil;a choc-m&eacute;tabolise du space marine brutal aux impulsions &eacute;lectro-magn&eacute;tiques !! 11! !!1", 295039237),
        ("&Ccedil;a d&eacute;sacralise du pirate fant&ocirc;me baroque avec un balai &agrave; chiottes !! 11! !!1", 6330703),
        ("&Ccedil;a g&eacute;nocide du vulcain soixante-huitard avec de l'hydrog&egrave;ne et du temps !! 11! !!1", 221017772),
        ("&Ccedil;a synchrotronne du Ch'ti contre nature &agrave; la kqlqsh !! 11! !!1", 9682974),
        ("&Ccedil;a d&eacute;soxyribe de l'oligarchie issu de la diversit&eacute; aux impulsions &eacute;lectro-magn&eacute;tiques !! 11! !!1", 189571452),
        ("&Ccedil;a gicle du trilobyte abracadabrantesque au frottis vaginal !! 11! !!1", 178919782),
        ("&Ccedil;a d&eacute;pote du gnome moldave &agrave; coups d'extincteur !! 11! !!1", 85905788),
        ("&Ccedil;a prol&eacute;tarise de l'ing&eacute;nieur gr&eacute;vistes au cocktail molotov !! 11! !!1", 65222857),
        ("&Ccedil;a vampirise du sbire peta-freudien &agrave; coups de pioche de Minecraft !! 11! !!1", 16443596),
        ("&Ccedil;a transplane du tib&eacute;tain mutant comme Marion Cotillard !! 11! !!1", 84163765),
        ("&Ccedil;a hashe du professeur d'anglais fukushimien de fa&ccedil;on th&eacute;&acirc;trale !! 11! !!1", 76825373),
        ("&Ccedil;a pl&acirc;tre du creep cubistes avec du caca !! 11! !!1", 124545540),
        ("&Ccedil;a poutre de l'huguenot volumique on the rocks !! 11! !!1", 193130668),
        ("&Ccedil;a d&eacute;soxyribe du zombi m&eacute;trique avec luxe, ccalme et volupt&eacute; !! 11! !!1", 92465520),
        ("&Ccedil;a d&eacute;plombe du p&eacute;gase rococo dans une cave !! 11! !!1", 194206770),
        ("&Ccedil;a endoctrine du lapin en plastique au frottis vaginal !! 11! !!1", 42355946),
        ("&Ccedil;a d&eacute;culotte du chaton silicon&eacute; au bromure !! 11! !!1", 235271031),
        ("&Ccedil;a mine du vulcain post-h&eacute;mophile dans un Sofitel !! 11! !!1", 2948014),
        ("&Ccedil;a carbonise du Corbier de deuxi&egrave;me g&eacute;n&eacute;ration comme dans du beurre !! 11! !!1", 178620425),
        ("&Ccedil;a d&eacute;pote de l'australopith&egrave;que d&eacute;pressif en mode nightmare !! 11! !!1", 231227348),
        ("&Ccedil;a indexe de l'octog&eacute;naire musulman dans un tentacle porn !! 11! !!1", 266233612),
        ("&Ccedil;a d&eacute;calcifie du Corbier testi-transsexuelophile au frottis vaginal !! 11! !!1", 145262649),
        ("&Ccedil;a dissout du Tutsi cryog&eacute;nis&eacute; au Decap four !! 11! !!1", 58399),
        ("&Ccedil;a g&eacute;nocide du golden retriever inter-volumique &agrave; coups de Bouda !! 11! !!1", 138714821),
        ("&Ccedil;a d&eacute;culotte du PDG callifragilistique &agrave; la grenade antichar !! 11! !!1", 157058511),
        ("&Ccedil;a d&eacute;pr&eacute;cate du diplodocus texan &agrave; coups de pioche de Minecraft !! 11! !!1", 112556498),
        ("&Ccedil;a d&eacute;gobille du mini-boss grand-guignolesque au choux de bruxelles !! 11! !!1", 249709594),
        ("&Ccedil;a saponifie du tyrannosaure peta-bouddhiste &agrave; la chambre &agrave; gaz !! 11! !!1", 122865139),
        ("&Ccedil;a d&eacute;soblige du trilobyte philat&eacute;liste au coup de pied Chuck Norris !! 11! !!1", 26507113),
        ("&Ccedil;a pollinise de l'iTruc rose invisible &agrave; la lime &agrave; ongle !! 11! !!1", 149873166),
        ("&Ccedil;a cocufie du footballeur cyber-triclass&eacute; (m&ecirc;me si &ccedil;a veut rien dire) !! 11! !!1", 79407636),
        ("&Ccedil;a tromblonne du g&eacute;niteur sous acide &agrave; coups d'extincteur !! 11! !!1", 222437030),
        ("&Ccedil;a destructure du retrait&eacute; unijambiste &agrave; coups de pain tueur !! 11! !!1", 248795927),
        ("&Ccedil;a licencie abusivement du raptor juda&iuml;stico-cryog&eacute;nis&eacute; avec emphase !! 11! !!1", 118914784),
        ("&Ccedil;a porcherise du pangolin phallocrate au b&acirc;ton de berger !! 11! !!1", 105447842),
        ("&Ccedil;a claque du kikoolol rutilant au coup de pied Chuck Norris !! 11! !!1", 47202043),
        ("&Ccedil;a bankablise du mouflon socio-gluant au cheval de Troie !! 11! !!1", 287651738),
        ("&Ccedil;a plaque-techtonise du creep exo-boulettesque &agrave; la chirurgie plastique !! 11! !!1", 41030181),
        ("&Ccedil;a d&eacute;pote du zergling en macram&eacute; dans le Space Mountain !! 11! !!1", 80383532),
        ("&Ccedil;a synchrotronne du ministre version shareware au karcher !! 11! !!1", 33772590),
        ("&Ccedil;a desquame du tib&eacute;tain mutant &agrave; la kqlqsh !! 11! !!1", 123840252),
        ("&Ccedil;a d&eacute;sacralise du vulcain abracadabrantesque au coup de pied Chuck Norris !! 11! !!1", 8229451),
        ("&Ccedil;a hashe du kilmoulis myxomateux en chantant \"que je t'aiiiiime\" !! 11! !!1", 8997701),
        ("&Ccedil;a caniculise du Tutsi n&eacute;o-narquois avec de l'hydrog&egrave;ne et du temps !! 11! !!1", 105918071),
        ("&Ccedil;a d&eacute;chire du lofteur verruqueux &agrave; la grenade vortex !! 11! !!1", 270944036),
        ("&Ccedil;a defibrille du python sarkozyste &agrave; la lime &agrave; ongle !! 11! !!1", 159483382),
        ("&Ccedil;a indexe du trilobyte testi-narquois de fa&ccedil;on th&eacute;&acirc;trale !! 11! !!1", 157653436),
        ("&Ccedil;a grattouille du Batman tentaculaire avec des hashtags litigieux !! 11! !!1", 215262617),
        ("&Ccedil;a plaque-techtonise du PDG rose caca d'oie avec un balai &agrave; chiottes !! 11! !!1", 34463997),
        ("&Ccedil;a charcle du secr&eacute;taire d'&eacute;tat bugg&eacute; avec des hashtags litigieux !! 11! !!1", 128504235),
        ("&Ccedil;a sodomise facialement de l'h&eacute;r&eacute;tique arabo-nymphomane avec luxe, ccalme et volupt&eacute; !! 11! !!1", 138334161),
        ("&Ccedil;a desquame du chaton psychopathe &agrave; la mitrailleuse g&eacute;ante de Counter-Strike !! 11! !!1", 255268800),
        ("&Ccedil;a licencie abusivement du missionnaire du zodiaque au sho-ryu-ken !! 11! !!1", 4492024),
        ("&Ccedil;a corrompt du mini-boss soixante-huitard en levrette !! 11! !!1", 253701209),
        ("&Ccedil;a synchrotronne du cercopith&egrave;que berserk au Famas !! 11! !!1", 2980494),
        ("&Ccedil;a d&eacute;calotte du gretchin mutant &agrave; coups d'extincteur !! 11! !!1", 109235896),
        ("&Ccedil;a sacque du retrait&eacute; myxomateux &agrave; la chambre &agrave; gaz !! 11! !!1", 154955072),
        ("&Ccedil;a brahmapoutre du p&eacute;on texan &agrave; la Holy Grenade !! 11! !!1", 54889803),
        ("&Ccedil;a g&eacute;nocide du pangolin national-iconoclaste au coup de pied Chuck Norris !! 11! !!1", 29811509),
        ("&Ccedil;a d&eacute;plombe du ninja ubuesque au karcher !! 11! !!1", 16389090),
        ("&Ccedil;a d&eacute;pote du roflcopter lvl 99 dans un tentacle porn !! 11! !!1", 68209448),
        ("&Ccedil;a viande du mini-boss baroque avec du Destop !! 11! !!1", 196352623),
        ("&Ccedil;a synchrotronne du papillon de lumi&egrave;re batave au pays des merveilles !! 11! !!1", 163108098),
        ("&Ccedil;a coup-critique du PDG endo-hermaphrodite dans un vortex !! 11! !!1", 194569710),
        ("&Ccedil;a d&eacute;calotte du papillon de lumi&egrave;re phallocrate dans le Space Mountain !! 11! !!1", 212001676),
        ("&Ccedil;a dissout du clapatte auto-disproportionn&eacute; &agrave; la grenade vortex !! 11! !!1", 265771123),
        ("&Ccedil;a chancre du Corbier batave au sho-ryu-ken !! 11! !!1", 241127977),
        ("&Ccedil;a pollinise du doppelganger callypige on the rocks !! 11! !!1", 101626002),
        ("&Ccedil;a g&eacute;nocide du clown disproportionn&eacute; au willy waller !! 11! !!1", 45335861),
        ("&Ccedil;a cristallise du lofteur juda&iuml;stico-verruqueux au fusil blaster !! 11! !!1", 31890841),
        ("&Ccedil;a r&eacute;chauffe climatiquement du Corbier peta-juif &agrave; l'&eacute;pilateur &eacute;lectrique !! 11! !!1", 171829950),
        ("&Ccedil;a endoctrine du kikoolol contre nature avec du Destop !! 11! !!1", 62417270),
        ("&Ccedil;a claque du dictateur v&eacute;reux avec le pouvoir de la Force !! 11! !!1", 165409771),
        ("&Ccedil;a poutre du sbire narquois au sho-ryu-ken !! 11! !!1", 61741648),
        ("&Ccedil;a d&eacute;moule du ninja en 3D filaire &agrave; la vol&eacute;e !! 11! !!1", 215573937),
        ("&Ccedil;a mine de la licorne boulettesque &agrave; la lame vorpale !! 11! !!1", 212066578),
        ("&Ccedil;a &eacute;chec-critique de l'oligarchie caf&eacute;&iuml;nomane &agrave; coups de petits cailloux dans les yeux !! 11! !!1", 83785903),
        ("&Ccedil;a pollinise du papillon de lumi&egrave;re &eacute;olien dans une maison en pain d'&eacute;pice !! 11! !!1", 119326662),
        ("&Ccedil;a prol&eacute;tarise du lol-politicien brutal au BFG !! 11! !!1", 293222737),
        ("&Ccedil;a auto-tamponne du creep gluant &agrave; la cyprine !! 11! !!1", 143128010),
        ("&Ccedil;a sacque du t&eacute;l&eacute;tubbies mega-emo &agrave; la massue en mousse !! 11! !!1", 59112632),
        ("&Ccedil;a lamine du punk rutilant au pays des merveilles !! 11! !!1", 240470055),
        ("&Ccedil;a d&eacute;sint&egrave;gre de la Barbie infra-kawaii en chantant \"que je t'aiiiiime\" !! 11! !!1", 228121668),
        ("&Ccedil;a porcherise du gretchin en armure de plates &agrave; la grenade vortex !! 11! !!1", 67510790),
        ("&Ccedil;a d&eacute;calcifie de l'h&eacute;r&eacute;tique para-cacahu&eacute;tovore &agrave; la mitrailleuse g&eacute;ante de Counter-Strike !! 11! !!1", 56187165),
        ("&Ccedil;a pollinise de l'albatros rose caca d'oie avec un petit coussin pour s'essuyer les doigts !! 11! !!1", 267693066),
        ("&Ccedil;a d&eacute;sacralise du lapin juda&iuml;stico-interop&eacute;rable &agrave; la d&eacute;loyale !! 11! !!1", 242721643),
        ("&Ccedil;a carbonise du chaton socio-berserk au double-clic !! 11! !!1", 96380261),
        ("&Ccedil;a zlatane de l'australopith&egrave;que r&eacute;cursif &agrave; la tringle &agrave; rideau !! 11! !!1", 163894918),
        ("&Ccedil;a mondialise du Ch'ti ex-batave &agrave; coups de petits cailloux dans les yeux !! 11! !!1", 154159125),
        ("&Ccedil;a auto-tamponne du pangolin sous licence libre dans un d&eacute; &agrave; coudre !! 11! !!1", 87669686),
        ("&Ccedil;a kill-steal du p&eacute;gase sous licence libre avec de l'hydrog&egrave;ne et du temps !! 11! !!1", 227073040),
        ("&Ccedil;a fragge du secr&eacute;taire d'&eacute;tat pestif&eacute;r&eacute; au cocktail molotov !! 11! !!1", 80889916),
        ("&Ccedil;a fraise de l'albatros para-gauchiste au fusil blaster !! 11! !!1", 52403936),
        ("&Ccedil;a merge du brontosaure fukushimien au gravier-cailloux-gros sel !! 11! !!1", 146209256),
        ("&Ccedil;a fertilise du raptor ubuesque dans un acc&eacute;l&eacute;rateur de particules !! 11! !!1", 236236893),
        ("&Ccedil;a d&eacute;culotte du Ch'ti roboratif &agrave; la d&eacute;loyale !! 11! !!1", 291896295),
        ("&Ccedil;a pistouille du golem de p&acirc;t&eacute; franco-verruqueux avec un balai &agrave; chiottes !! 11! !!1", 237748971),
        ("&Ccedil;a rushe du missionnaire nymphomane au Chanel num&eacute;ro 5 !! 11! !!1", 144104023),
        ("&Ccedil;a plaque-techtonise du zergling testi-tentaculaire en levrette !! 11! !!1", 100813581),
        ("&Ccedil;a kill-steal du golden retriever cacahu&eacute;tovore &agrave; la lime &agrave; ongle !! 11! !!1", 42158464),
        ("&Ccedil;a g&eacute;nocide du schtroumpf kawaii au patator !! 11! !!1", 100347389),
        ("&Ccedil;a rushe du trilobyte endo-contractuel en chantant une chanson paillarde !! 11! !!1", 152550487),
        ("&Ccedil;a poutre du kilmoulis racaillou avec un nuage de lait !! 11! !!1", 274102804),
        ("&Ccedil;a blat&egrave;re du raptor catho-journalistique au Baygon !! 11! !!1", 67830311),
        ("&Ccedil;a d&eacute;gobille du cercopith&egrave;que taylorien en mode nightmare !! 11! !!1", 37172938),
        ("&Ccedil;a pistouille du pingouin Linux soixante-huitard &agrave; la lame vorpale !! 11! !!1", 78534507),
        ("&Ccedil;a blat&egrave;re du sbire anarcho-gauchiste &agrave; la vol&eacute;e !! 11! !!1", 242000723),
        ("&Ccedil;a sacque du gnome sous-r&ocirc;liste &agrave; l'&eacute;pilateur &eacute;lectrique !! 11! !!1", 10230104),
        ("&Ccedil;a cyclotronne de l'ing&eacute;nieur n&eacute;o-kawaii avec luxe, ccalme et volupt&eacute; !! 11! !!1", 79600445),
        ("&Ccedil;a g&eacute;nocide du clown callypige &agrave; coups de pain tueur !! 11! !!1", 77034941),
        ("&Ccedil;a broute-minoutte du p&eacute;on endo-libidineux dans la joie et la bonne humeur !! 11! !!1", 112000990),
        ("&Ccedil;a caresse du hamster inverti au sabre laser !! 11! !!1", 207466185),
        ("&Ccedil;a chattouille de l'albatros ante-roboratif en chantant une chanson paillarde !! 11! !!1", 227008156),
        ("&Ccedil;a d&eacute;plombe de l'ewok m&eacute;cano-anarchiste dans la joie et la bonne humeur !! 11! !!1", 225257742),
        ("&Ccedil;a pollinise du p&eacute;gase national-guerrier-mage-clerc &agrave; la touche windows !! 11! !!1", 256457286),
        ("&Ccedil;a cale&ccedil;onne du zergling exo-journalistique sur l'air du Gangnam Style !! 11! !!1", 228928371),
        ("&Ccedil;a d&eacute;gobille du commercial g&eacute;latineux au Chanel num&eacute;ro 5 !! 11! !!1", 24884374),
        ("&Ccedil;a blat&egrave;re du Michel Drucker rouge et jaune &agrave; petit pois en chantant une chanson paillarde !! 11! !!1", 182466371),
        ("&Ccedil;a sodomise facialement du schtroumpf du 16&egrave;me si&egrave;cle dans un vortex !! 11! !!1", 200272485),
        ("&Ccedil;a caresse de l'ewok droitiste &agrave; la disquette 3 pouces et demi !! 11! !!1", 55526601),
        ("&Ccedil;a fraise du lapin unijambiste dans un vortex !! 11! !!1", 144146804),
        ("&Ccedil;a paup&eacute;rise du doppelganger nymphomane au missile magique !! 11! !!1", 67279391),
        ("&Ccedil;a d&eacute;plombe de la prostate version shareware avec le pouvoir de la Force !! 11! !!1", 218115378),
        ("&Ccedil;a g&eacute;nocide du hamster contractuel dans un vortex !! 11! !!1", 63859481),
        ("&Ccedil;a gicle du creep m&eacute;cano-philat&eacute;liste &agrave; la chambre &agrave; gaz !! 11! !!1", 84267394),
        ("&Ccedil;a vilipende du clown kawaii &agrave; l'acide chlorhydrique !! 11! !!1", 293736266),
        ("&Ccedil;a l&eacute;galise du lol-politicien spermovore en chantant une chanson paillarde !! 11! !!1", 55484922),
        ("&Ccedil;a endoctrine du gnome rococo in the clouds !! 11! !!1", 242275286),
        ("&Ccedil;a grattouille du retrait&eacute; japonais dans un acc&eacute;l&eacute;rateur de particules !! 11! !!1", 16135349),
        ("&Ccedil;a copeaute du footballeur hydroc&eacute;phale avec un nuage de lait !! 11! !!1", 78231288),
        ("&Ccedil;a d&eacute;plombe du paladin &eacute;olien &agrave; la d&eacute;loyale !! 11! !!1", 37444770),
        ("&Ccedil;a mondialise de l'h&eacute;r&eacute;tique maxi-grand-guignolesque au Spero Patronum !! 11! !!1", 39059205),
        ("&Ccedil;a fork du g&eacute;niteur du 16&egrave;me si&egrave;cle &agrave; l'allocation universelle !! 11! !!1", 278799941),
        ("&Ccedil;a auto-tamponne du caniche de combat version beta au missile magique !! 11! !!1", 41894102),
        ("&Ccedil;a licencie abusivement de l'acad&eacute;micien macro-brutal au cocktail molotov !! 11! !!1", 187390888),
        ("&Ccedil;a d&eacute;pr&eacute;cate du Corbier macro-cul-de-jatte &agrave; la touche windows !! 11! !!1", 131772614),
        ("&Ccedil;a d&eacute;r&eacute;glemente du smiley mucoviscideux dans un acc&eacute;l&eacute;rateur de particules !! 11! !!1", 113225828),
        ("&Ccedil;a indexe de l'elfe clignotant au sho-ryu-ken !! 11! !!1", 112893808),
        ("&Ccedil;a blat&egrave;re du secr&eacute;taire g&eacute;n&eacute;ral UMP myxomateux en buzzant &agrave; donf !! 11! !!1", 50944295),
        ("&Ccedil;a fragge du footballeur exo-roboratif au cheval de Troie !! 11! !!1", 280465816),
        ("&Ccedil;a mine de l'ing&eacute;nieur en plastique au cheval de Troie !! 11! !!1", 1664434),
        ("&Ccedil;a cocufie du missionnaire bouddhiste dans un d&eacute; &agrave; coudre !! 11! !!1", 173787648),
        ("&Ccedil;a d&eacute;soblige de l'ogre-mage cyber-v&eacute;reux avec le pouvoir de la Force !! 11! !!1", 117630385),
        ("&Ccedil;a pr&eacute;carise de l'humoriste crypto-unijambiste &agrave; coups de blashp&egrave;mes !! 11! !!1", 223263576),
        ("&Ccedil;a desquame du professeur d'anglais sous acide au moule &agrave; gauffre !! 11! !!1", 30881844),
        ("&Ccedil;a d&eacute;grade du roflcopter sur-ind&eacute;pendantiste comme dans du beurre !! 11! !!1", 273864111),
        ("&Ccedil;a choc-m&eacute;tabolise du roflcopter verruqueux au willy waller !! 11! !!1", 182800885),
        ("&Ccedil;a pr&eacute;carise du lapin nazi au fer &agrave; friser !! 11! !!1", 188263908),
        ("&Ccedil;a trucide du ministre sous licence libre au gravier-cailloux-gros sel !! 11! !!1", 33660696),
        ("&Ccedil;a copeaute du cercopith&egrave;que infra-rococo au disrupteur dimensionnel !! 11! !!1", 271160976),
        ("&Ccedil;a copeaute du diplodocus narquois &agrave; la r&acirc;pe &agrave; fromage !! 11! !!1", 140203416),
        ("&Ccedil;a choc-m&eacute;tabolise du ninja tentaculaire en buzzant &agrave; donf !! 11! !!1", 260528701),
        ("&Ccedil;a bravitudifie de l'ewok guerrier-mage-clerc dans un h&ocirc;tel borgne !! 11! !!1", 278114245),
        ("&Ccedil;a head-shote du trooper sous licence libre au bizutage !! 11! !!1", 200080018),
        ("&Ccedil;a broute-minoutte du raptor para-journalistique dans une maison en pain d'&eacute;pice !! 11! !!1", 174467110),
        ("&Ccedil;a tatane du secr&eacute;taire g&eacute;n&eacute;ral UMP version beta dans un Sofitel !! 11! !!1", 247644887),
        ("&Ccedil;a blat&egrave;re du commercial nymphomane &agrave; la chambre &agrave; gaz !! 11! !!1", 220147031),
        ("&Ccedil;a rushe de l'h&eacute;r&eacute;tique para-anarchiste &agrave; la r&acirc;pe &agrave; fromage !! 11! !!1", 269932555),
        ("&Ccedil;a trucide du trooper arabo-cacahu&eacute;tovore on the rocks !! 11! !!1", 119567460),
        ("&Ccedil;a gicle du kikoolol abracadabrantesque dans un acc&eacute;l&eacute;rateur de particules !! 11! !!1", 180569482),
        ("&Ccedil;a commit du caniche de combat g&eacute;latineux avec luxe, ccalme et volupt&eacute; !! 11! !!1", 235977510),
        ("&Ccedil;a prol&eacute;tarise du schtroumpf rose caca d'oie dans une cave !! 11! !!1", 276424309),
        ("&Ccedil;a lamine de l'acad&eacute;micien disproportionn&eacute; avec un petit coussin pour s'essuyer les doigts !! 11! !!1", 193268007),
        ("&Ccedil;a d&eacute;pucelle du gitan rutilant &agrave; coups de pioche de Minecraft !! 11! !!1", 140822114),
        ("&Ccedil;a cristallise du vulcain juda&iuml;stico-myxomateux avec de l'hydrog&egrave;ne et du temps !! 11! !!1", 182700637),
        ("&Ccedil;a charcle du hamster gobelettoforme au sho-ryu-ken !! 11! !!1", 189370551),
        ("&Ccedil;a l&eacute;galise du ninja silicon&eacute; au fer &agrave; friser !! 11! !!1", 14338758),
        ("&Ccedil;a synchrotronne de l'ing&eacute;nieur infra-emo &agrave; la touche windows !! 11! !!1", 18641142),
        ("&Ccedil;a prol&eacute;tarise du tyrannosaure endo-moldave au b&acirc;ton de berger !! 11! !!1", 126915805),
    )

    for (expression, seed) in TEST_DATA:
        assert generate_expression(seed) == expression

