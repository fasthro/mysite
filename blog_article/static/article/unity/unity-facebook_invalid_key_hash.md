
### 接入 Facebook  SDK 登录的时候提示Hash Key无效

<a class="pop-img-box" href="http://localhost:8000/static/article/unity/img/facebook_invalid_key_hash/facebook_invalid_key_hash.png"><img src="http://localhost:8000/static/article/unity/img/facebook_invalid_key_hash/facebook_invalid_key_hash.png" alt=""></a>

这个问题主要原因是由于facebook后台配置的hash key不正确导致。

如果应用在google play 市场，应用使用了Google Play App 签名，那么facebook 后台的hash key 就不能用官方的方法来生成，因为google会重新给应用签名，这样会导致最终在google play 下载下来的应用的hash key改变，最终导致hash key 无效的问题。

打开google play 后台，把 SHA1 转成 base64 就会得到一个25为的 hash key。
<a class="pop-img-box" href="http://localhost:8000/static/article/unity/img/facebook_invalid_key_hash/img1.png"><img src="http://localhost:8000/static/article/unity/img/facebook_invalid_key_hash/img1.png" alt=""></a>

通过 [http://tomeko.net/online_tools/hex_to_base64.php?](http://tomeko.net/online_tools/hex_to_base64.php?) 工具转把 SHA1 转成 base64的 hase key。

<a class="pop-img-box" href="http://localhost:8000/static/article/unity/img/facebook_invalid_key_hash/img2.png"><img src="http://localhost:8000/static/article/unity/img/facebook_invalid_key_hash/img2.png" alt=""></a>

最终把这个hase key 填到facebook 的后台就可以了（注意这样测试必须要从google play市场下载应用进行facebook登录）。