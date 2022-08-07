import tarfile,os
from UI2.data import globalparam
#打包测试报告
#打包文件夹  'w:gz'压缩并且打包
def make_targz(out_filename,source_dir):
    '''

    :param out_filename: 打包后tar文件
    :param source_dir: 需要打包的文件夹
    :return:
    '''
    with tarfile.open(out_filename,'w:gz') as tar:
        tar.add(source_dir,arcname=os.path.basename(source_dir))




make_targz(globalparam.image_path+'out.tar',globalparam.image_path)