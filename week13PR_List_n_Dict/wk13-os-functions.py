#!/usr/bin/env python3.10
# Name: Do Hyung Kim
# Date: 4/10/2023
# Title: Exploring the files and the directories on a Linux operating system using Python.
import os, sys

print("get the path of current working directory")
path = os.getcwd()

print("using walk() method and nested for loops to display all the files and directories") 
for root, directories, files in os.walk(path, topdown=False):
	for name in files:
		print("file: ", os.path.join(root, name))
	for name in directories:
		print("folder: ", os.path.join(root, name))


print("\n##########################")
print("listdir() method was used to display all the files and directories on your current workingdirectory.")
files = os.listdir(path)
for f in files:
	print(f)

print("\n##########################")
print("Let's traverse an entire directory tree under your current working directory.")
wd  = os.getcwd()
directories = os.walk(wd)
dirpath, dirnames, filenames = next(directories)
print("Directory Path:", dirpath)
print("Directory Names:", dirnames)
print("File Names:", filenames)
print("\n##########################")


dirpath, dirnames, filenames = next(directories)
print("Directory Path:", dirpath)
print("Directory Names:", dirnames)
print("File Names:", filenames)
print("\n##########################")

dirpath, dirnames, filenames = next(directories)
print("Directory Path:", dirpath)
print("Directory Names:", dirnames)
print("File Names:", filenames)
print("\n##########################")

dirpath, dirnames, filenames = next(directories)
print("Directory Path:", dirpath)
print("Directory Names:", dirnames)
print("File Names:", filenames)
print("\n##########################")



'''

1. The following output demonstrates how os.walk() method walks through 
	all the sub directories and all the files under current working directory. 
2. Instead of using for loop, the next() method was used 
   to manually trigger the traversal of the entire tree directory 
   starting from the top (your current working directory) to the botton.


Output: 
~/my-python-repo$ ./week13/wk13-os-functions.py
get the path of current working directory
using walk() method and nested for loops to display all the files and directories
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/fsmonitor-watchman.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/push-to-checkout.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/update.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/pre-applypatch.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/pre-push.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/pre-receive.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/pre-merge-commit.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/applypatch-msg.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/pre-commit.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/prepare-commit-msg.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/commit-msg.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/post-update.sample
file:  /home/dohyungkim2023/my-python-repo/.git/hooks/pre-rebase.sample
file:  /home/dohyungkim2023/my-python-repo/.git/objects/49/643f1f2687790aa54b9c066a5c303e7b530f0e
file:  /home/dohyungkim2023/my-python-repo/.git/objects/52/8b11654c973a9fd1d30cca7746b1989a84d0aa
file:  /home/dohyungkim2023/my-python-repo/.git/objects/c5/65835127d3055fd14927dd5644cca075b84dbb
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7d/287af85a3a917e3ae6f4085b44e45d5e9b3e5f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7d/928b1ee8ddcdd4d2de61219b9d48190e57f26d
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e3/3d9011c1307a3d6eceb5a796be9a7121fcb329
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e3/e83ecd35e8f75eca5b4400a320ad0c27cf0ec4
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7c/68f4aafcb40a040100f86f122148d1765c1abd
file:  /home/dohyungkim2023/my-python-repo/.git/objects/ad/0bfc9860c05866da5cb074379abb189a3f38d8
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a2/b1fde369283c0aae5847fba2e635d666112091
file:  /home/dohyungkim2023/my-python-repo/.git/objects/44/e91f48ddd90ca5b30ca4b6d07f3b48fcc496ab
file:  /home/dohyungkim2023/my-python-repo/.git/objects/3e/02c256775bfba9516bdb6a69f2dea5e0d54399
file:  /home/dohyungkim2023/my-python-repo/.git/objects/30/bdfd802123c72180ef2a02dc80b729be4b84ca
file:  /home/dohyungkim2023/my-python-repo/.git/objects/f5/b1518f34f1473117f1170e96e86345190c8d33
file:  /home/dohyungkim2023/my-python-repo/.git/objects/5b/b4097d5112118577f618488f29e59fa1990241
file:  /home/dohyungkim2023/my-python-repo/.git/objects/5b/836af98a0821787f2a7b8292535a27cc6d088c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b4/fd8f400b07573940da882f5f1f69856057be3e
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b0/db908dc9b902458ca3619f65bbf31c0174c3d1
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b0/ec75214984034f96d9d20ccab1a475a83aca7e
file:  /home/dohyungkim2023/my-python-repo/.git/objects/8c/00630e0e4ba8ff1395ab48258f738e9aa99af9
file:  /home/dohyungkim2023/my-python-repo/.git/objects/51/ffc52f125dbfefa6669a2371b39ff0c76b1695
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a8/b4964f6c3a87f27faab9bd670656957ab01fa8
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a8/5225a0ce546492e8138a283873e50512268044
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a8/4021b0641b86c33c748a40f0a3517e182486da
file:  /home/dohyungkim2023/my-python-repo/.git/objects/bd/3aba3c41e36b11d0605ee91f2b8940950f65aa
file:  /home/dohyungkim2023/my-python-repo/.git/objects/bd/43c57c4f276dff983b3fa1eea25b63413fcd11
file:  /home/dohyungkim2023/my-python-repo/.git/objects/6b/426a519a7a65f7aef9bfa9a60f7200ac7e2124
file:  /home/dohyungkim2023/my-python-repo/.git/objects/55/189ea76ed6d6f154245f467346675d966916fd
file:  /home/dohyungkim2023/my-python-repo/.git/objects/55/48d1e3a25e1ab5793b8651d894f29296cee398
file:  /home/dohyungkim2023/my-python-repo/.git/objects/86/0c00594ae75ca8ec2f1ecbc21dd1b06bff69b4
file:  /home/dohyungkim2023/my-python-repo/.git/objects/df/fca6d33fde52fb73d66cb2cec201641fb22a8c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/8b/9201506d17e10935cab341abf3403fc0fab1df
file:  /home/dohyungkim2023/my-python-repo/.git/objects/07/081d9d3778d79f8358839d337d7362bfc1fa4d
file:  /home/dohyungkim2023/my-python-repo/.git/objects/15/1309920de6d161f251f4f527f2e2ba5a784d53
file:  /home/dohyungkim2023/my-python-repo/.git/objects/15/a1d717d75979fd412b3faed51f4cb34740c2dc
file:  /home/dohyungkim2023/my-python-repo/.git/objects/15/5b7a5fd67e2c460966144abbc3d673f63fc4cf
file:  /home/dohyungkim2023/my-python-repo/.git/objects/1e/3caea0585fc90c7f1d1a4cd9a6b0b1619a1336
file:  /home/dohyungkim2023/my-python-repo/.git/objects/79/b04af55b52006dd4e77e9f7b1c58690601e941
file:  /home/dohyungkim2023/my-python-repo/.git/objects/79/a221e97a644a94d2a290fff52607c5514cebef
file:  /home/dohyungkim2023/my-python-repo/.git/objects/bb/1ba790a3ca1a2de7cdccb5942617e1ace6bd58
file:  /home/dohyungkim2023/my-python-repo/.git/objects/24/206c4d129cc3ca3fa03aa204a14de820609e02
file:  /home/dohyungkim2023/my-python-repo/.git/objects/6a/a6d559918d3a22f38b8628f9a685bcd720b90e
file:  /home/dohyungkim2023/my-python-repo/.git/objects/3b/fba49af95e18b2a96a64661c7b7c5a043733cb
file:  /home/dohyungkim2023/my-python-repo/.git/objects/3b/a1ec3f81e9f27ef1a03bf64ba7863033c9807b
file:  /home/dohyungkim2023/my-python-repo/.git/objects/12/1101ae5553a457bc5ea51c393683c5bc819af2
file:  /home/dohyungkim2023/my-python-repo/.git/objects/bc/db0c253e3122380a94bb72f97af683a5f221d6
file:  /home/dohyungkim2023/my-python-repo/.git/objects/f2/2c338f4806a135e349a35aa89d3b65aa1e9266
file:  /home/dohyungkim2023/my-python-repo/.git/objects/pack/pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.pack
file:  /home/dohyungkim2023/my-python-repo/.git/objects/pack/pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.idx
file:  /home/dohyungkim2023/my-python-repo/.git/objects/39/0fc4105e38ad77ba4af26915c7c8c4938116a1
file:  /home/dohyungkim2023/my-python-repo/.git/objects/fe/dd72890cd1e67ceb128ada17d74dc9a9e48e8d
file:  /home/dohyungkim2023/my-python-repo/.git/objects/fe/fa9d82db3038e37b1b66188665adf819761497
file:  /home/dohyungkim2023/my-python-repo/.git/objects/fe/e918db9d682b5b72afaa0380ffc308e95b1fe6
file:  /home/dohyungkim2023/my-python-repo/.git/objects/cf/68c5c767b37ca1da86e7ef7787179bb9f92d3d
file:  /home/dohyungkim2023/my-python-repo/.git/objects/89/d2d529acb7b3eec35eb253eaad3d2d560561ea
file:  /home/dohyungkim2023/my-python-repo/.git/objects/56/8059592871c1af40ab29184ee72ac1b4fa6256
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a9/39dcfb58ea56b075d0d9a20e04ccad0680aade
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a9/b715aa58581aae109876cd4b943834b53da2e0
file:  /home/dohyungkim2023/my-python-repo/.git/objects/5c/592fd7f7d3d6f0aefc6c7e6e45d1ec530057ef
file:  /home/dohyungkim2023/my-python-repo/.git/objects/5c/629f6f736c2399279ee7ab0bc2d28fb15fec70
file:  /home/dohyungkim2023/my-python-repo/.git/objects/db/ff3b0ede55191a9c1794f1b16caeb0f512851c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/db/c5e624e52b3600f60321ed9c01220f760d2940
file:  /home/dohyungkim2023/my-python-repo/.git/objects/db/c8ad028bf4647fb621e5a836c421a805c3c897
file:  /home/dohyungkim2023/my-python-repo/.git/objects/f8/d5d1c35d69a126e0f0d00b2e18fded21dae18a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/f8/3488d50435da081d04272f8a9f421c3fca0024
file:  /home/dohyungkim2023/my-python-repo/.git/objects/61/563060fd251ec7a59f7640627f4ac9be965f8a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/8f/04b5aa8d81b80c98310a7de08e971449a67465
file:  /home/dohyungkim2023/my-python-repo/.git/objects/8f/b0f0ab6204966eafa3ca4eb4c160c1ff655cf4
file:  /home/dohyungkim2023/my-python-repo/.git/objects/d0/ba861cd519bce06732c63c594dc2fe151c6ac8
file:  /home/dohyungkim2023/my-python-repo/.git/objects/da/0f4ef9d638bf1771feb75196285faab00f636f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/fd/84e220aadc3997f7fd9e692da8b989cf4ea523
file:  /home/dohyungkim2023/my-python-repo/.git/objects/2e/8b658b034ee863a505ac60f69e93833f0dfeae
file:  /home/dohyungkim2023/my-python-repo/.git/objects/77/af61b5e0da01cdf7ee65a51cff5126cc22c05c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e1/0b9e03b8b4ded7022d28f13cad3a5234ec0a8b
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a4/2a34aee20dd0cc48cb07380cc1185e3ae34e69
file:  /home/dohyungkim2023/my-python-repo/.git/objects/05/24cbdcd374d58f9fe916af757873132f7ee761
file:  /home/dohyungkim2023/my-python-repo/.git/objects/cd/2628560a9c20fbf5bde25ad75df07717bc44ee
file:  /home/dohyungkim2023/my-python-repo/.git/objects/cd/57ec51d6528b92ae854c39797800a56793ba0f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/4e/56e999470e8fea5b33bf166521043e61ebf21a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/57/39ca7bcd15400233caba1c2837324eff0581a2
file:  /home/dohyungkim2023/my-python-repo/.git/objects/1f/17d9d2aa9216156ec305041b4af962f33c0324
file:  /home/dohyungkim2023/my-python-repo/.git/objects/2d/feca495a97bbe68f80ead23b9a180b3f016b4f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7a/a14c719238ba6ab4ad189959c7139b1b673aed
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7a/0e4e6490879ab51ab5f950c3b163ea3942a713
file:  /home/dohyungkim2023/my-python-repo/.git/objects/9a/da4f7af78af440a5dbffd659b8c07b69d9deb6
file:  /home/dohyungkim2023/my-python-repo/.git/objects/9a/1d7c1c1cd9e40f56809a9f602d4dc7f65c30ff
file:  /home/dohyungkim2023/my-python-repo/.git/objects/87/2192097cd47d4aabc96a290362a78914031857
file:  /home/dohyungkim2023/my-python-repo/.git/objects/d1/c9460bbfe8ed3998144c61e3cad22476ea9196
file:  /home/dohyungkim2023/my-python-repo/.git/objects/d1/54061b8c4e2c477e239d3a3b4cc1091bdece75
file:  /home/dohyungkim2023/my-python-repo/.git/objects/c4/db043e639574c668321a15b9fe9449d485710d
file:  /home/dohyungkim2023/my-python-repo/.git/objects/11/34d4c525753dbf2b7b67c6a2dbbcbcc5141dc5
file:  /home/dohyungkim2023/my-python-repo/.git/objects/11/2e3fa45e7a3066403586af9c8b732298cbf2fb
file:  /home/dohyungkim2023/my-python-repo/.git/objects/4a/21f73359a1041ee825a3b90a221737df66360a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/04/4ace1ce598045b3f6e144b86a363938e468d22
file:  /home/dohyungkim2023/my-python-repo/.git/objects/ef/1d0aa6c117b712c88f5f5b85b8785878abec21
file:  /home/dohyungkim2023/my-python-repo/.git/objects/ef/770e80243fa8b983b7c460ae10fa8f94080a16
file:  /home/dohyungkim2023/my-python-repo/.git/objects/91/445d045d48af5ac657eb4e57236affbf957319
file:  /home/dohyungkim2023/my-python-repo/.git/objects/70/f87e88c40362500f354d5ba0cb19c36ff9dffd
file:  /home/dohyungkim2023/my-python-repo/.git/objects/70/efc0e9308124404b7dac3bf1d18514f7497fbc
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7e/2eac4fb2c2b50ddfdedc3be41fa57dbeb0bd89
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7e/94229fabe95566121299ecdc96732378999a5d
file:  /home/dohyungkim2023/my-python-repo/.git/objects/3f/8acedfc8c2781a22bf6f359bcee9345750f6ed
file:  /home/dohyungkim2023/my-python-repo/.git/objects/de/b2b7dffe81dae9747eaf28d555227390a4eef4
file:  /home/dohyungkim2023/my-python-repo/.git/objects/0e/397a5bac8d47df962c710719e7f79d31769787
file:  /home/dohyungkim2023/my-python-repo/.git/objects/4d/0cad273b78f9ce5ec8cfa7223ef02804a46d33
file:  /home/dohyungkim2023/my-python-repo/.git/objects/f3/00cd16db6b883fa518abd447da5711734553dc
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b2/42bdcca03f0488714b078cd0005f8bccc634a6
file:  /home/dohyungkim2023/my-python-repo/.git/objects/85/24c6b4b47627abea364661a1e10821e5e5060f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/85/f5a01de7c56e79c5ae50edc6dcb9a0cb048aa6
file:  /home/dohyungkim2023/my-python-repo/.git/objects/03/4b92b1e2ff5ad46af3aaa6b07c453da225dc06
file:  /home/dohyungkim2023/my-python-repo/.git/objects/60/ee7ff66a4e24815a19ab6a15bead0e47157c4a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/60/f9e859e5263392d33b03497072e861a6a50e47
file:  /home/dohyungkim2023/my-python-repo/.git/objects/ba/5a2aebfef323fff7e8b5f3d097c4e06a75f40e
file:  /home/dohyungkim2023/my-python-repo/.git/objects/ec/da58750c3637d01fc9f560f74c6998fca70450
file:  /home/dohyungkim2023/my-python-repo/.git/objects/ec/b7ec65bb946cc74c9d4f7cfe465d382c988cfa
file:  /home/dohyungkim2023/my-python-repo/.git/objects/ea/e7f62b0516c65b4bc8a47a1fe1b78707057e35
file:  /home/dohyungkim2023/my-python-repo/.git/objects/09/127f9e344851b97eff4639fd1c101e78881e1c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/09/b012e77630215158a34813ad624b4691a1a986
file:  /home/dohyungkim2023/my-python-repo/.git/objects/80/e20920fb732fa585230f43947b322d1799ac9f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/67/1b28ccee7ddae70faa0a53eb0781d189d65c42
file:  /home/dohyungkim2023/my-python-repo/.git/objects/a7/21c62629648d6caefd3d5f6e19580730d96413
file:  /home/dohyungkim2023/my-python-repo/.git/objects/1d/bba33dac22c791e86c3ccfa51c9b16f082f02a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/13/d8f8378b80496f778fd5c2660bcaa9fceb0a8c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/13/24716327e824d34d0e3ad907d1c27729b2dd1f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/32/696ee6c5b102d64d16df6e768cb99b0b35926a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/32/8d69ce0d59c5175ff58b47e87325ae3e3b52d5
file:  /home/dohyungkim2023/my-python-repo/.git/objects/99/8d0486e5e00f4c759743ec478546c54f338968
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b6/779320394da6f4484bc926683d21ac41196b54
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b6/f777725f0000abc51738efdbd413deaee48e36
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e8/bfcf8ce4f9be67019cedb45f1b5265693f6e18
file:  /home/dohyungkim2023/my-python-repo/.git/objects/26/c3a1c490466b6d9e9aa65b04b8e02f34d13a0b
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b1/9c779b1749ef6badecbc74a6e2b3646bbf790a
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b1/336a948e9eb6a9d3eb06c93e287ff6f1d0d91c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/1b/fcb3f5f9d27524136b744d4a6b907e412ee5ab
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e0/fdef9563b110ef1925bfa6544acb10cf16fbc2
file:  /home/dohyungkim2023/my-python-repo/.git/objects/0c/fc551ba8c25d1330b421d22b2b2125ee5d8a6f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/5d/49ebb685c5b602a58d909b7d7bb4949542a48b
file:  /home/dohyungkim2023/my-python-repo/.git/objects/5d/b10daf8245892c7fe874dffe59abe45ef12d78
file:  /home/dohyungkim2023/my-python-repo/.git/objects/1a/a0a95110d1c19e9de7308d2e3ffb2594faa6e3
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7b/1cc34cff9ff511d166ad4b71dd0e052ac8fb1d
file:  /home/dohyungkim2023/my-python-repo/.git/objects/7b/11c8c687a57780b9baf1038cc22efbd9f78422
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e7/abc8b9014da7209cf242c1ff948e8feddc23b8
file:  /home/dohyungkim2023/my-python-repo/.git/objects/fc/52f07c3c82b3df2deaf49200ab2a56c14175f8
file:  /home/dohyungkim2023/my-python-repo/.git/objects/fc/a03bab2fcd8d039a7998af59a15f3de173f8c0
file:  /home/dohyungkim2023/my-python-repo/.git/objects/d9/fea6ac86159840757f30565dbda375e79ba39f
file:  /home/dohyungkim2023/my-python-repo/.git/objects/6c/5f11fcb426454c02847c6b795354fff776cab4
file:  /home/dohyungkim2023/my-python-repo/.git/objects/eb/01d12a6335d005c5276a8d2dc634452a64bd1c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/84/d41bc3d2fbc8faa86f8b4dfed887b412a4b92b
file:  /home/dohyungkim2023/my-python-repo/.git/objects/97/538fb7f1403c182ac1af1b4e77bea4d67e0db9
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e5/309aa67ed69b926490a44f0b6b76518b64ee29
file:  /home/dohyungkim2023/my-python-repo/.git/objects/54/402fbf718bdccd6231740f7db1a192dd0b49d5
file:  /home/dohyungkim2023/my-python-repo/.git/objects/c8/b8bf481cc58a43b4927caf04c4bdb0e1d58da6
file:  /home/dohyungkim2023/my-python-repo/.git/objects/38/6838c905ce704e33c4eaa205211714ed9e0e39
file:  /home/dohyungkim2023/my-python-repo/.git/objects/17/61e3eff0243b7c3f93f1846e38c635540200e1
file:  /home/dohyungkim2023/my-python-repo/.git/objects/c2/ae9d8e619633e3611372b6a7c6ebd979cc56a9
file:  /home/dohyungkim2023/my-python-repo/.git/objects/c2/e33ef95f6f2cb20dabaa77274576ff984f4b49
file:  /home/dohyungkim2023/my-python-repo/.git/objects/62/b69a0aedacf895ce57c84e7331500a04c12097
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b7/ebfcccb1369a2d8828ca0c77080a7d3a33dfc6
file:  /home/dohyungkim2023/my-python-repo/.git/objects/6e/540a6c0e7ca18ec97fd1e5d6d3be3577422572
file:  /home/dohyungkim2023/my-python-repo/.git/objects/6e/63693a9b4e96d5edb28fd6178ff7633ce0a2e5
file:  /home/dohyungkim2023/my-python-repo/.git/objects/b9/c3c09c68c5fa940719c0df51f4ad94ff5c086c
file:  /home/dohyungkim2023/my-python-repo/.git/objects/e9/d85e4cc767f8c076c9498b9d2b618a357384ca
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/49
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/52
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/c5
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/7d
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/e3
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/7c
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/ad
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/a2
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/44
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/3e
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/30
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/f5
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/5b
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/b4
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/b0
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/8c
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/51
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/a8
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/bd
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/6b
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/55
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/86
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/df
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/8b
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/07
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/15
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/1e
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/79
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/bb
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/24
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/6a
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/3b
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/12
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/bc
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/f2
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/pack
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/39
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/fe
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/cf
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/89
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/56
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/a9
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/5c
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/db
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/f8
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/61
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/8f
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/d0
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/da
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/fd
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/2e
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/77
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/e1
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/a4
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/05
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/cd
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/4e
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/57
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/1f
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/2d
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/7a
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/9a
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/87
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/d1
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/c4
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/11
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/4a
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/04
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/ef
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/91
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/70
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/7e
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/3f
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/de
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/0e
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/4d
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/f3
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/b2
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/85
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/03
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/60
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/ba
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/ec
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/ea
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/09
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/80
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/67
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/a7
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/1d
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/13
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/32
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/99
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/info
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/b6
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/e8
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/26
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/b1
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/1b
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/e0
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/0c
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/5d
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/1a
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/7b
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/e7
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/fc
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/d9
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/6c
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/eb
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/84
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/97
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/e5
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/54
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/c8
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/38
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/17
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/c2
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/62
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/b7
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/6e
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/b9
folder:  /home/dohyungkim2023/my-python-repo/.git/objects/e9
file:  /home/dohyungkim2023/my-python-repo/.git/info/exclude
file:  /home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin/main
folder:  /home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin
file:  /home/dohyungkim2023/my-python-repo/.git/refs/heads/main
file:  /home/dohyungkim2023/my-python-repo/.git/refs/heads/dkim-04102023
folder:  /home/dohyungkim2023/my-python-repo/.git/refs/tags
folder:  /home/dohyungkim2023/my-python-repo/.git/refs/remotes
folder:  /home/dohyungkim2023/my-python-repo/.git/refs/heads
file:  /home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin/main
folder:  /home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin
file:  /home/dohyungkim2023/my-python-repo/.git/logs/refs/heads/main
file:  /home/dohyungkim2023/my-python-repo/.git/logs/refs/heads/dkim-04102023
folder:  /home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes
folder:  /home/dohyungkim2023/my-python-repo/.git/logs/refs/heads
file:  /home/dohyungkim2023/my-python-repo/.git/logs/HEAD
folder:  /home/dohyungkim2023/my-python-repo/.git/logs/refs
file:  /home/dohyungkim2023/my-python-repo/.git/index
file:  /home/dohyungkim2023/my-python-repo/.git/HEAD
file:  /home/dohyungkim2023/my-python-repo/.git/packed-refs
file:  /home/dohyungkim2023/my-python-repo/.git/config
file:  /home/dohyungkim2023/my-python-repo/.git/description
file:  /home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD
file:  /home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG
file:  /home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD
folder:  /home/dohyungkim2023/my-python-repo/.git/branches
folder:  /home/dohyungkim2023/my-python-repo/.git/hooks
folder:  /home/dohyungkim2023/my-python-repo/.git/objects
folder:  /home/dohyungkim2023/my-python-repo/.git/info
folder:  /home/dohyungkim2023/my-python-repo/.git/refs
folder:  /home/dohyungkim2023/my-python-repo/.git/logs
file:  /home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v1.py
file:  /home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v3.py
file:  /home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v4_list_of_dict.py
file:  /home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v5_dict_of_dict.py
file:  /home/dohyungkim2023/my-python-repo/week13/wk13-project_list_v1.py
file:  /home/dohyungkim2023/my-python-repo/week13/wk13-project_file_dict_1st_draft.py
file:  /home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v2.py
file:  /home/dohyungkim2023/my-python-repo/week13/output.txt
file:  /home/dohyungkim2023/my-python-repo/week12/wk12-project_AWS-service-inventory.py
file:  /home/dohyungkim2023/my-python-repo/testing-functions.py
file:  /home/dohyungkim2023/my-python-repo/string-info.py
file:  /home/dohyungkim2023/my-python-repo/scopes.py
file:  /home/dohyungkim2023/my-python-repo/.gitignore
file:  /home/dohyungkim2023/my-python-repo/fizz-buzz.py
file:  /home/dohyungkim2023/my-python-repo/py-if-elif-else.py
file:  /home/dohyungkim2023/my-python-repo/using-dictionaries.py
file:  /home/dohyungkim2023/my-python-repo/README.md
file:  /home/dohyungkim2023/my-python-repo/find_string.py
file:  /home/dohyungkim2023/my-python-repo/split&join_again.py
file:  /home/dohyungkim2023/my-python-repo/scope2.py
file:  /home/dohyungkim2023/my-python-repo/fizz-buzz-item.py
file:  /home/dohyungkim2023/my-python-repo/wk13-Mon-lesson-04032023.py
file:  /home/dohyungkim2023/my-python-repo/using-list.py
file:  /home/dohyungkim2023/my-python-repo/variations.py
file:  /home/dohyungkim2023/my-python-repo/Hello_world.py
file:  /home/dohyungkim2023/my-python-repo/Hello_yourname.py
file:  /home/dohyungkim2023/my-python-repo/using-generator.py
folder:  /home/dohyungkim2023/my-python-repo/.git
folder:  /home/dohyungkim2023/my-python-repo/week13
folder:  /home/dohyungkim2023/my-python-repo/week12

##########################
listdir() method was used to display all the files and directories on your current workingdirectory.
testing-functions.py
string-info.py
scopes.py
.gitignore
fizz-buzz.py
py-if-elif-else.py
using-dictionaries.py
README.md
find_string.py
split&join_again.py
.git
scope2.py
fizz-buzz-item.py
wk13-Mon-lesson-04032023.py
using-list.py
variations.py
week13
Hello_world.py
Hello_yourname.py
week12
using-generator.py

##########################
Let's traverse an entire directory tree under your current working directory.
Directory Path: /home/dohyungkim2023/my-python-repo
Directory Names: ['.git', 'week13', 'week12']
File Names: ['testing-functions.py', 'string-info.py', 'scopes.py', '.gitignore', 'fizz-buzz.py', 'py-if-elif-else.py', 'using-dictionaries.py', 'README.md', 'find_string.py', 'split&join_again.py', 'scope2.py', 'fizz-buzz-item.py', 'wk13-Mon-lesson-04032023.py', 'using-list.py', 'variations.py', 'Hello_world.py', 'Hello_yourname.py', 'using-generator.py']

##########################
Directory Path: /home/dohyungkim2023/my-python-repo/.git
Directory Names: ['branches', 'hooks', 'objects', 'info', 'refs', 'logs']
File Names: ['index', 'HEAD', 'packed-refs', 'config', 'description', 'FETCH_HEAD', 'COMMIT_EDITMSG', 'ORIG_HEAD']

##########################
Directory Path: /home/dohyungkim2023/my-python-repo/.git/branches
Directory Names: []
File Names: []

##########################
Directory Path: /home/dohyungkim2023/my-python-repo/.git/hooks
Directory Names: []
File Names: ['fsmonitor-watchman.sample', 'push-to-checkout.sample', 'update.sample', 'pre-applypatch.sample', 'pre-push.sample', 'pre-receive.sample', 'pre-merge-commit.sample', 'applypatch-msg.sample', 'pre-commit.sample', 'prepare-commit-msg.sample', 'commit-msg.sample', 'post-update.sample', 'pre-rebase.sample']

##########################

'''