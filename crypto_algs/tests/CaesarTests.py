import pytest
from crypto_algs.Caesar import Caesar


# sequence assertions

def setup_module(module):
    # init_something()
    pass


def teardown_module(module):
    # teardown_something()
    pass


def test_encrypt_zero_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 0) == b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c'


def test_encrypt_single_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 1) == b'\xd2\x93\xd2\xb2\xd2\xbb\xd3\x84\xd3\x8d'


def test_encrypt_256_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 256) ==\
           b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c'


def test_encrypt_255_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 255) == \
           b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'


def test_encrypt_42_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 42) == \
           b'\xfb\xbc\xfb\xdb\xfb\xe4\xfc\xad\xfc\xb6'


def test_decrypt_encrypted_sequence():
    for i in range(300):
        assert Caesar.decrypt(Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', i), i) == \
               b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c'


def test_decrypt_encrypted_sequence_without_shift():
    assert Caesar.decrypt_without_shift(b'\xff') == [b'\xff', b'\xfe', b'\xfd',
                                                     b'\xfc', b'\xfb', b'\xfa',
                                                     b'\xf9', b'\xf8', b'\xf7',
                                                     b'\xf6', b'\xf5', b'\xf4',
                                                     b'\xf3', b'\xf2', b'\xf1',
                                                     b'\xf0', b'\xef', b'\xee',
                                                     b'\xed', b'\xec', b'\xeb',
                                                     b'\xea', b'\xe9', b'\xe8',
                                                     b'\xe7', b'\xe6', b'\xe5',
                                                     b'\xe4', b'\xe3', b'\xe2',
                                                     b'\xe1', b'\xe0', b'\xdf',
                                                     b'\xde', b'\xdd', b'\xdc',
                                                     b'\xdb', b'\xda', b'\xd9',
                                                     b'\xd8', b'\xd7', b'\xd6',
                                                     b'\xd5', b'\xd4', b'\xd3',
                                                     b'\xd2', b'\xd1', b'\xd0',
                                                     b'\xcf', b'\xce', b'\xcd',
                                                     b'\xcc', b'\xcb', b'\xca',
                                                     b'\xc9', b'\xc8', b'\xc7',
                                                     b'\xc6', b'\xc5', b'\xc4',
                                                     b'\xc3', b'\xc2', b'\xc1',
                                                     b'\xc0', b'\xbf', b'\xbe',
                                                     b'\xbd', b'\xbc', b'\xbb',
                                                     b'\xba', b'\xb9', b'\xb8',
                                                     b'\xb7', b'\xb6', b'\xb5',
                                                     b'\xb4', b'\xb3', b'\xb2',
                                                     b'\xb1', b'\xb0', b'\xaf',
                                                     b'\xae', b'\xad', b'\xac',
                                                     b'\xab', b'\xaa', b'\xa9',
                                                     b'\xa8', b'\xa7', b'\xa6',
                                                     b'\xa5', b'\xa4', b'\xa3',
                                                     b'\xa2', b'\xa1', b'\xa0',
                                                     b'\x9f', b'\x9e', b'\x9d',
                                                     b'\x9c', b'\x9b', b'\x9a',
                                                     b'\x99', b'\x98', b'\x97',
                                                     b'\x96', b'\x95', b'\x94',
                                                     b'\x93', b'\x92', b'\x91',
                                                     b'\x90', b'\x8f', b'\x8e',
                                                     b'\x8d', b'\x8c', b'\x8b',
                                                     b'\x8a', b'\x89', b'\x88',
                                                     b'\x87', b'\x86', b'\x85',
                                                     b'\x84', b'\x83', b'\x82',
                                                     b'\x81', b'\x80', b'\x7f',
                                                     b'\x7e', b'\x7d', b'\x7c', b'\x7b', b'\x7a',
                                                     b'\x79', b'\x78', b'\x77', b'\x76', b'\x75',
                                                     b'\x74', b'\x73', b'\x72', b'\x71', b'\x70',
                                                     b'\x6f', b'\x6e', b'\x6d', b'\x6c', b'\x6b',
                                                     b'\x6a', b'\x69', b'\x68', b'\x67', b'\x66',
                                                     b'\x65', b'\x64', b'\x63', b'\x62', b'\x61',
                                                     b'\x60', b'\x5f', b'\x5e', b'\x5d', b'\x5c',
                                                     b'\x5b', b'\x5a', b'\x59', b'\x58', b'\x57',
                                                     b'\x56', b'\x55', b'\x54', b'\x53', b'\x52',
                                                     b'\x51', b'\x50', b'\x4f', b'\x4e', b'\x4d',
                                                     b'\x4c', b'\x4b', b'\x4a', b'\x49', b'\x48',
                                                     b'\x47', b'\x46', b'\x45', b'\x44', b'\x43',
                                                     b'\x42', b'\x41', b'\x40', b'\x3f', b'\x3e',
                                                     b'\x3d', b'\x3c', b'\x3b', b'\x3a', b'\x39',
                                                     b'\x38', b'\x37', b'\x36', b'\x35', b'\x34',
                                                     b'\x33', b'\x32', b'\x31', b'\x30', b'\x2f',
                                                     b'\x2e', b'\x2d', b'\x2c', b'\x2b', b'\x2a',
                                                     b'\x29', b'\x28', b"\x27", b'\x26', b'\x25',
                                                     b'\x24', b'\x23', b'\x22', b'\x21', b'\x20',
                                                     b'\x1f', b'\x1e', b'\x1d', b'\x1c',
                                                     b'\x1b', b'\x1a', b'\x19', b'\x18',
                                                     b'\x17', b'\x16', b'\x15', b'\x14',
                                                     b'\x13', b'\x12', b'\x11', b'\x10',
                                                     b'\x0f', b'\x0e', b'\r', b'\x0c',
                                                     b'\x0b', b'\n', b'\t', b'\x08',
                                                     b'\x07', b'\x06', b'\x05', b'\x04',
                                                     b'\x03', b'\x02', b'\x01', b'\x00']


# text assertions

def test_encrypt_zero_shift_ru():
    assert 'Съешь еще этих мягких французских булок да выпей чаю же!' == \
           Caesar.encrypt_text('Съешь еще этих мягких французских булок да выпей чаю же!', 0, 'ru')


def test_encrypt_single_shift_ru():
    assert 'Тыжщэ жъж юуйц надлйц хсбочфитлйц вфмпл еб гьржк шбя зж!' == \
           Caesar.encrypt_text('Съешь еще этих мягких французских булок да выпей чаю же!', 1, 'ru')


def test_encrypt_32_shift_ru():
    assert 'Съешь еще этих мягких французских булок да выпей чаю же!' == \
           Caesar.encrypt_text('Съешь еще этих мягких французских булок да выпей чаю же!', 32, 'ru')


def test_encrypt_31_shift_ru():
    assert 'Рщдчы дшд ьсзф лювйзф упямхтжрйзф аткнй гя бъоди цяэ ед!' == \
           Caesar.encrypt_text('Съешь еще этих мягких французских булок да выпей чаю же!', 31, 'ru')


def test_encrypt_43_shift_ru():
    assert 'Ьергз рдр иэуа чкохуа яылшбютьхуа мюцщх пл нжърф влй ср!' == \
           Caesar.encrypt_text('Съешь еще этих мягких французских булок да выпей чаю же!', 43, 'ru')


def test_decrypt_encrypted_sequence_ru():
    for i in range(300):
        assert Caesar.decrypt_text(
            Caesar.encrypt_text('Съешь еще этих мягких французских булок да выпей чаю же!', i, 'ru'), i, 'ru') == \
               'Съешь еще этих мягких французских булок да выпей чаю же!'


def test_decrypt_encrypted_text_without_shift_ru():
    assert Caesar.decrypt_text_without_shift('Съешь еще этих мягких французских булок да выпей чаю же!', 'ru') \
           == ['Съешь еще этих мягких французских булок да выпей чаю же!',
               'Тыжщэ жъж юуйц надлйц хсбочфитлйц вфмпл еб гьржк шбя зж!',
               'Уьзъю зыз яфкч обемкч цтвпшхйумкч гхнрм жв дэсзл щва из!',
               'Фэиыя иьи ахлш пвжнлш чугрщцкфнлш дцосн зг еютим ъгб йи!',
               'Хюйьа йэй бцмщ ргзомщ шфдсъчлхомщ ечпто ид жяуйн ыдв кй!',
               'Цякэб кюк вчнъ сдипнъ щхетышмцпнъ жшруп йе зафко ьег лк!',
               'Чалюв лял гшоы тейроы ъцжуьщнчроы зщсфр кж ибхлп эжд мл!',
               'Шбмяг мам дщпь ужкспь ычзфэъошспь иътхс лз йвцмр юзе нм!',
               'Щвнад нбн еърэ фзлтрэ ьшихюыпщтрэ йыуцт ми кгчнс яиж он!',
               'Ъгобе ово жысю химусю эщйцяьръусю кьфчу нй лдшот айз по!',
               'Ыдпвж пгп зьтя цйнфтя юъкчаэсыфтя лэхшф ок мещпу бки рп!',
               'Ьергз рдр иэуа чкохуа яылшбютьхуа мюцщх пл нжърф влй ср!',
               'Эжсди сес йюфб шлпцфб аьмщвяуэцфб нячъц рм озысх гмк тс!',
               'Юзтей тжт кяхв щмрчхв бэнъгафючхв оашыч сн пиьтц днл ут!',
               'Яиужк узу лацг ънсшцг вюоыдбхяшцг пбщьш то рйэуч еом фу!',
               'Айфзл фиф мбчд ыотщчд гяпьевцащчд рвъэщ уп скюфш жпн хф!',
               'Бкхим хйх нвше ьпуъше дарэжгчбъше сгыюъ фр тляхщ зро цх!',
               'Влцйн цкц огщж эрфыщж ебсюздшвыщж тдьяы хс умацъ исп чц!',
               'Гмчко члч пдъз юсхьъз жвтяиещгьъз уеэаь цт фнбчы йтр шч!',
               'Дншлп шмш реыи ятцэыи згуайжъдэыи фжюбэ чу ховшь кус щш!',
               'Еощмр щнщ сжьй аучюьй идфбкзыеюьй хзявю шф цпгщэ лфт ъщ!',
               'Жпънс ъоъ тзэк бфшяэк йехвлиьжяэк циагя щх чрдъю мху ыъ!',
               'Зрыот ыпы уиюл вхщаюл кжцгмйэзаюл чйбда ъц шсеыя нцф ьы!',
               'Исьпу ьрь фйям гцъбям лзчднкюибям шквеб ыч щтжьа очх эь!',
               'Йтэрф эсэ хкан дчыван мишеоляйван щлгжв ьш ъузэб пшц юэ!',
               'Куюсх ютю цлбо ешьгбо нйщжпмакгбо ъмдзг эщ ыфиюв рщч яю!',
               'Лфятц яуя чмвп жщэдвп окъзрнблдвп ынеид юъ ьхйяг съш ая!',
               'Мхауч афа шнгр зъюегр плыисовмегр ьожйе яы эцкад тыщ ба!',
               'Нцбфш бхб щодс иыяждс рмьйтпгнждс эпзкж аь ючлбе уьъ вб!',
               'Очвхщ вцв ъпет йьазет снэкурдозет юрилз бэ яшмвж фэы гв!',
               'Пшгцъ гчг ыржу кэбижу тоюлфсепижу ясйми вю ащнгз хюь дг!',
               'Рщдчы дшд ьсзф лювйзф упямхтжрйзф аткнй гя бъоди цяэ ед!']


def test_encrypt_zero_shift_en():
    assert 'The quick brown fox jumps over the lazy dog.' == \
           Caesar.encrypt_text('The quick brown fox jumps over the lazy dog.', 0, 'en')


def test_encrypt_single_shift_en():
    assert 'Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.' == \
           Caesar.encrypt_text('The quick brown fox jumps over the lazy dog.', 1, 'en')


def test_encrypt_26_shift_en():
    assert 'The quick brown fox jumps over the lazy dog.' == \
           Caesar.encrypt_text('The quick brown fox jumps over the lazy dog.', 26, 'en')


def test_encrypt_25_shift_en():
    assert 'Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf.' == \
           Caesar.encrypt_text('The quick brown fox jumps over the lazy dog.', 25, 'en')


def test_encrypt_43_shift_en():
    assert 'Kyv hlztb sifne wfo aldgj fmvi kyv crqp ufx.' == \
           Caesar.encrypt_text('The quick brown fox jumps over the lazy dog.', 43, 'en')


def test_decrypt_encrypted_sequence_en():
    for i in range(300):
        assert Caesar.decrypt_text(
            Caesar.encrypt_text('The quick brown fox jumps over the lazy dog.', i, 'en'), i, 'en') == \
               'The quick brown fox jumps over the lazy dog.'


def test_decrypt_encrypted_text_without_shift_en():
    assert Caesar.decrypt_text_without_shift('The quick brown fox jumps over the lazy dog.', 'en') \
           == ['The quick brown fox jumps over the lazy dog.',
               'Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.',
               'Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi.',
               'Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj.',
               'Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk.',
               'Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl.',
               'Znk waoiq hxuct lud pasvy ubkx znk rgfe jum.',
               'Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.',
               'Bpm ycqks jzwev nwf rcuxa wdmz bpm tihg lwo.',
               'Cqn zdrlt kaxfw oxg sdvyb xena cqn ujih mxp.',
               'Dro aesmu lbygx pyh tewzc yfob dro vkji nyq.',
               'Esp bftnv mczhy qzi ufxad zgpc esp wlkj ozr.',
               'Ftq cguow ndaiz raj vgybe ahqd ftq xmlk pas.',
               'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.',
               'Hvs eiwqy pfckb tcl xiadg cjsf hvs zonm rcu.',
               'Iwt fjxrz qgdlc udm yjbeh dktg iwt apon sdv.',
               'Jxu gkysa rhemd ven zkcfi eluh jxu bqpo tew.',
               'Kyv hlztb sifne wfo aldgj fmvi kyv crqp ufx.',
               'Lzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy.',
               'Max jnbvd ukhpg yhq cnfil hoxk max etsr whz.',
               'Nby kocwe vliqh zir dogjm ipyl nby futs xia.',
               'Ocz lpdxf wmjri ajs ephkn jqzm ocz gvut yjb.',
               'Pda mqeyg xnksj bkt fqilo kran pda hwvu zkc.',
               'Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.',
               'Rfc osgai zpmul dmv hsknq mtcp rfc jyxw bme.',
               'Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf.']


