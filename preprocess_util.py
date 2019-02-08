import torchvision.transforms as transforms

class PreprocessUtil():
    def __init__(self, ):
        pass


    def parseTransform(self, names):
        lst = []
        for name in names.split('_'):
            if "resize" in name:
                value = name.strip("resize")
                lst += [transforms.Resize(self._parse_x(value))]
            elif "normalize" in name:
                value = self._parse_comma(name.strip("normalize"))
                lst += [transforms.Normalize(value[0:3], value[3:6])]
            elif "toTensor" in name:
                lst += [transforms.ToTensor()]
            elif "randomCrop" in name:
                value = name.strip("randomCrop")
                lst += [transforms.RandomCrop(self._parse_x(value))]
            elif "centerCrop" in name:
                value = name.strip("centerCrop")
                lst += [transforms.CenterCrop(self._parse_x(value))]
            elif "randomVerticalFlip" in name:
                lst += [transforms.RandomVerticalFlip()]
            elif "randomResizedCrop" in name:
                v = self._parse_comma(name.strip("randomResizedCrop"))
                lst += [transforms.RandomResizedCrop(int(v[0]), v[1:3], v[3:5], int(v[5]))]
            elif "grayScale" in name:
                value = int(name.strip("grayScale"))
                lst += [transforms.grayScale(value)]
            elif "randomRotation" in name:
                striped_name = name.strip("randomRotation")
                if ',' in striped_name:
                    v = self._parse_comma(striped_name)
                else:
                    v = int(striped_name)
                lst += [transforms.RandomRotation(v)]
            elif "randomGrayscale" in name:
                v = float(value)
                lst += [transforms.RandomGrayscale(v)]
            elif "toPILImage" in name:
                lst += [transforms.ToPILImage()]
            elif "randomHorizontalFlip" in name:
                lst += [transforms.RandomHorizontalFlip()]
            elif "randomVerticalFlip" in name:
                lst += [transforms.RandomVerticalFlip()]
            elif "randomBackground" in name:
                lst += [transforms.RandomBackground(self.setting['data']['base'])]
            elif "pad" in name:
                striped_name = name.strip("pad")
                v = int(striped_name)
                lst += [transforms.Pad(v)]
            elif "colorJitter" in name:
                v = self._parse_comma(name.strip("colorJitter"))
                # default
                # transforms.ColorJitter(brightness=0, contrast=0, saturation=0, hue=0)
                lst += [transforms.ColorJitter(brightness=v[0], contrast=v[1], saturation=v[2], hue=v[3])]
            elif 'toNumpy' in name:
                lst += [my_transforms.ToNumpy()]
            elif 'correctExif' in name:
                lst += [my_transforms.CorrectExif()]
            elif 'humanCrop' in name:
                value = self._parse_comma(name.strip("humanCrop"))
                lst += [my_transforms.HumanCrop(margin=value[0], weight_path=self.setting['dataset']['openPosePath'], scale=value[1], gpu_ids=str(int(value[2])))]
            elif name == 'None':
    
                pass
            else:
                raise NotImplementedError("{} is could not parse, this function is not implemented.".format(name))
            
        return transforms.Compose(lst)

    def _parse_x(self, value):
        if "x" in value:
            value = [int(x) for x in value.split("x")]
        else:
            value = int(value)

        return value

    def _parse_comma(self, value):
        if "," in value:
            ret = []
            for x in value.split(','):
                if 'x' in x:
                    ret += [self._parse_x(x)]
                else:
                    ret += [float(x)]
                    
        else:
            raise ValueError("comma is needed")
        return ret
