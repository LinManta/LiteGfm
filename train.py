from __future__ import absolute_import, division, print_function

from options import LiteGfmOptions
from trainer import Trainer

options = LiteGfmOptions()
opts = options.parse()        #自定义的各种设置


if __name__ == "__main__":    #
    trainer = Trainer(opts)   #设置赋给训练器
    trainer.train()
