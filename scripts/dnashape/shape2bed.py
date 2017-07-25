import os
from itertools import islice
import numpy as np
def shape2bed(input_file_name,output_file_name):
    with open(input_file_name) as fin, open(output_file_name,'w') as fout:
        write_content = []
        for line in fin:
            if '>' in line:
                if write_content != []:
                    values = write_content[3:]
                    has_values = []
                    for v in values:
                        try:
                            has_values.append(float(v))
                        except ValueError:
                            pass
                    write_content = write_content[:3]
                    if has_values == []:
                        write_content.extend(['na','na','na'])
                    else:
                        write_content.append(str(min(has_values)))
                        write_content.append(str(max(has_values)))
                        write_content.append(str(np.median(has_values)))
                    fout.write('\t'.join(write_content))
                    fout.write(os.linesep)
                    write_content = []
                temp = line.rstrip(os.linesep)
                temp = temp.lstrip('>')
                temp = temp.split(':')
                write_content.append(temp[0])
                temp = temp[1].split('-')
                write_content.append(temp[0])
                write_content.append(temp[1])
            else:
                temp = line.rstrip(os.linesep)
                write_content.extend(temp.split(','))
        if write_content != []:
            values = write_content[3:]
            has_values = []
            for v in values:
                try:
                    has_values.append(float(v))
                except ValueError:
                    pass
            write_content = write_content[:3]
            if has_values == []:
                write_content.extend(['na','na','na'])
            else:
                write_content.append(str(min(has_values)))
                write_content.append(str(max(has_values)))
                write_content.append(str(np.median(has_values)))
            fout.write('\t'.join(write_content))
            fout.write(os.linesep)
        fin.close()
        fout.close()
shape2bed('../../data/processed/train_regions.blacklistfiltered.fa.HelT','../../data/processed/train_shape_feature_HelT.bed')
shape2bed('../../data/processed/train_regions.blacklistfiltered.fa.Roll','../../data/processed/train_shape_feature_Roll.bed')
shape2bed('../../data/processed/train_regions.blacklistfiltered.fa.ProT','../../data/processed/train_shape_feature_ProT.bed')
shape2bed('../../data/processed/train_regions.blacklistfiltered.fa.MGW','../../data/processed/train_shape_feature_MGW.bed')
shape2bed('../../data/processed/test_regions.blacklistfiltered.fa.HelT','../../data/processed/test_shape_feature_HelT.bed')
shape2bed('../../data/processed/test_regions.blacklistfiltered.fa.Roll','../../data/processed/test_shape_feature_Roll.bed')
shape2bed('../../data/processed/test_regions.blacklistfiltered.fa.ProT','../../data/processed/test_shape_feature_ProT.bed')
shape2bed('../../data/processed/test_regions.blacklistfiltered.fa.MGW','../../data/processed/test_shape_feature_MGW.bed')
