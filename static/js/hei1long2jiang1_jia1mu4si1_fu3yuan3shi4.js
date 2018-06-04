(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('抚远市', {"type":"FeatureCollection","features":[{"type":"Feature","id":"230883","properties":{"name":"抚远市","cp":[134.307884,48.364687],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@[aP{q@@DuA@@@CBA@CBABABCDC@GDABABC@@BAA@@CB@@AACAC@AAAAABA@AAA@AAA@@AAAAAA@CAC@@@AC@BA@A@A@A@CAAAA@A@A@A@@@@A@@AAA@A@A@CACAA@ABCA@BA@CAABA@@@ACA@C@C@AAA@A@A@@BA@@BAB@@A@@@@B@@C@ABA@GFIAAFCBA@CDCBEBABAB@DA@EDA@@@AAA@A@AB@@A@AA@AC@CACAAAA@A@A@A@AA@BABA@E@CA@@ABA@CBA@AA@AA@A@A@C@CAA@A@C@A@ABAAA@A@G@A@C@A@ABAB@BABC@CBA@AAA@A@CBA@C@A@@@A@AB@@@@A@@BA@ABC@A@ABAB@@C@@@AB@@A@A@C@A@@@A@ABA@A@@@C@C@@AA@@@@@A@@@@@AAA@AA@@ACA@A@AAA@@@AAC@ABA@@@@@@@ABA@AA@@A@A@A@@@A@A@A@@@C@@AA@@A@A@@@AA@AAA@@@@@AAAAA@@@C@@@A@AA@@CA@@C@ABA@@@A@@B@@A@A@@@A@EBA@AAA@@@@@A@@@A@AA@@A@@B@@A@@AA@C@E@A@AAC@@@@@ABA@A@C@ABA@AB@@@@BB@@C@@B@@A@A@@@A@@@A@C@A@A@C@AB@@AAC@ABA@@@AAA@E@C@@@A@@A@@A@CAC@@@A@@BAAAB@@A@@A@@@@A@@@A@I@@BA@@B@BA@@@A@AAE@A@@@@@A@@B@@@B@@@B@@AB@@DD@B@BA@A@@B@B@F@F@D@D@F@D@D@D@@@B@D@D@D@BAD@B@D@B@D@B@D@B@D@B@B@B@D@D@B@@@F@H@B@F@LAnAt@D@P@@@\\Ad@\\@bAZ@V@L@NAN@N@L@B@B@B@@ADAB@BBD@F@B@B@BEDCDEFAD@DABED@B@BDD@B@F@DÚLJNRLDn`VLbB`L`VTVfHJÖBB@@A@@@CBA@@@@BBB@@B@BB@@A@A@E@AB@@B@BBB@@@DAB@@@B@@BAD@BA@@@BB@@BABAB@@@BB@@A@AB@@A@A@@@BBB@B@@@BA@AB@B@FDB@D@FBD@@@@@D@B@B@B@BBBB@DB@@@B@B@DCBAB@BB@B@@@BB@B@@@@A@@@ACA@A@@@@@ABAB@@@DB@@B@B@@@@A@AA@@@@AB@DADAB@BBBB@B@B@@@BC@@B@@CBB@BB@@BB@@AB@@BBBBB@@@BB@@A@AB@@@B@@A@@@@C@@A@@BA@@B@@@@BBD@BB@@@@A@A@@@@B@@A@@@A@A@ADAB@@BBBDB@AB@@B@BAB@@@@@@BA@ABB@@@B@DCB@@@@@BBB@DBB@D@B@B@@B@B@BB@B@@@@@@AA@@AB@BAB@BB@@@BCF@@@@B@D@@AB@A@@A@@@AD@D@@BB@@B@@B@@A@A@AB@B@@@@ACA@@@A@@B@B@F@@BB@BAB@B@B@BB@@B@DCFA@AA@@A@@D@@@B@B@@@B@BDB@@B@BB@B@@@B@B@@@@B@@B@@@@@BA@@BB@B@@@@B@BA@A@@@@B@B@BB@@B@@A@@B@BA@@@@@@A@@AA@@@BA@BB@B@BBB@BBBB@@A@A@B@@BB@B@B@B@BB@A@@B@@A@@B@@@B@@@AB@BB@@@DAB@@BBB@@@@A@@BB@@B@@C@@@ABB@BBB@@BA@@@A@@@AA@A@@A@AB@BB@@B@B@BB@@@B@@AB@@@D@@@@B@@@@B@@@AABA@@@@BB@@@B@@A@@BA@BB@@AB@B@@@@AB@@@A@@@AB@@@@AA@A@@@ABBB@@@B@B@@B@@B@@A@@@A@BBBBB@B@D@B@B@@@AAA@@AB@@@B@BBABB@@B@@A@@@@BD@@@@@@BA@@@DDB@@A@A@@B@B@@@BB@BAB@@BB@A@@@AB@B@@@BB@B@@DB@@B@@A@@@ABAB@B@@B@B@@BB@A@@@AB@B@@B@BB@BA@@BA@AB@@@B@@B@@AB@@B@B@B@BBB@@@@B@@AB@@@BAA@AA@@@@BA@@BBB@@AB@@@B@@BB@@BB@@@B@BA@A@A@@@B@BBF@B@B@@@ABB@@B@@BA@@@ABB@@A@@B@@B@BA@@@@B@@@@B@@@@@@B@@BA@@B@@@@B@B@@@@@@@A@BBBA@@@@AB@@@@B@@@BB@@@@ABA@@@@D@@@@@@A@@@BB@@@@A@A@BB@@@@BA@B@@@@A@A@@BA@@@@@@AA@@B@B@B@@@@B@@@B@@B@@@AB@@B@BB@@BB@@A@AB@BB@@@@AB@@A@BB@@@@@@B@@A@@@B@@@B@B@@B@@@@@@@B@@@@BB@@BA@@@@@@@@@B@@@B@@@AB@@@@B@B@@AA@B@@@B@@B@@@@AB@@@@BBB@@@AB@@D@@@@@@BA@@AA@A@@@BB@@BB@@A@@@A@@@@BD@@@A@@@@@A@A@@@@BBBBA@@B@B@@@@@@BA@@@@@@@@BB@@@@@@@BA@@@BBBA@A@@@@B@B@@@@BAB@@@@@@@BA@@@B@@@@AB@@A@A@B@B@B@@B@@A@@@BBB@@@@@@@C@@@@@BBBB@@@@A@@@ABA@@@@A@B@@@@@BF@@@AB@@@BB@DA@@@B@@A@@@@B@@BBBB@CB@BB@@B@@@@ADB@BAB@@@@D@@BBAB@@B@@@@@@B@B@@@B@@B@@A@A@@@A@@@@BB@B@@B@@A@AAA@@B@@@B@D@@@@B@B@BB@@AB@@@@B@@@B@B@B@AB@@B@@@B@@@@@@B@@B@B@A@@BA@@@@BB@@@@@@B@@@BC@@@A@A@@B@@B@@@CB@@@B@@A@@@@B@@@@D@BB@@@B@@@@@B@@A@@B@@B@BA@@@BA@AB@@@@BB@@@@C@ABBB@@@BC@@BA@BBA@B@@BB@@BB@BAD@AAA@@AB@@@BBBBA@@@@B@B@@A@@@@BB@B@@@@BA@A@@BABB@B@B@@@@@@@ABC@ABABA@C@A@@AD@A@C@ABCBAB@D@BA@A@@@A@A@AB@B@@@@@@ABABADAB@@ABA@A@AA@@AACAA@A@@@A@ABA@A@A@@@AB@B@B@BABA@@@A@@@CAABADCDCDGLILGJCD@@EBABC@ABCD@D@B@DB@@BB@@BB@@BDBB@BB@B@BADCBEBC@EBABADA@E@@BA@C@@@A@@BA@A@@B@@@B@@DB@@BAB@B@B@B@@BB@B@B@B@@B@@@BC@A@@B@B@@A@@@@@A@AAA@AAA@A@@@AAA@A@AAA@A@A@@@AB@@A@@B@@@@@@@@@@AB@@@@AB@@A@A@AAA@A@@@@@ABADADADADCFA@@DELM`B@PJfd^NZFXB`ElETB`DhVVT^\\XN`L\\BnARGNANDbHfBhELATCd@hJdN`JtNTHVD\\D`FRD^HTBV@XCRCdKdGX@PBbBvD`CTCdB\\@PCZOx_ZMNI`@rDbHZN^XPZPVNP`ZRJ^JRDRD^AT@dKxIdAV@VDVJRRNHNBTGRKNQBE@SCU@KAIAEQOSIWGQGWEQE]MOIUEWEQCWAMCMCKGGCWA_@WGA@SqQGACAgSIIY_QEa@_KCCGCKAG@ICGCEEIGKAA@A@Q@WB_UC_AMDKCqNYKQ@C@@GOACLOBC@C@EEGECKEOGGEGGIIIKKSEKAUQO[MOQocCMCMACeIGIDS@CBGDE@CBEBAAEAEAAAAAAAA@AAC@AAC@A@@@CBCBCBCBCJIDADADCBADABABALCDCJGTOPKFIJKDK@UCURGdA\\APCD@BADABAJGNMHEAMAEEICK@OBABGBCBGBE@EBCAOACBIFInUNGFAPGFCFCDC\\]rQRMFIRe@KIcEEKIEEECIICCACAAACEACEIGCACAA@AA@A@@@AAAAAAACAAACACACAACIKIKMIECCCCCCAEAAACC@AGCCAAAIICSBEBGBO@IM]ME[KY_QMQUMGCCEAGEEAECCACAiMIKBk@AIUCGAAAC@AA@AACAEAA@C@C@C@C@Q@CAA@CAC@MEEAIAqeBlHæBfDFÒB\\@FBdBnA@@N@DD²©DEUHQWCCa]M@GiBSIMCGOYFEKEGMWMYIEJGIORGRCFM@OKEKWLI@OMIYMGCIO@CBSAKQCUAMMCCTOOQQAIIGAIKEG[NMOU@Y@DK@AcGaKJQQMIEOFEUAOKMMA[De`X"],"encodeOffsets":[[137328,48760]]}}],"UTF8Encoding":true});}));