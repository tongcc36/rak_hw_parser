import xmltodict

primaryParams = {}

with open("BIOS.txt", "r") as fp:
    for _line in fp.readlines():
        if len(_line) <= 0:
            continue
        primaryParam = _line.split("->")[-1]
        primaryParamName = primaryParam.split("=")[0].strip().replace("\n", "").lower()
        primaryParamValue = primaryParam.split("=")[1].strip().replace("\n", "")
        primaryParams[primaryParamName] = primaryParamValue
        pass
    pass

with open("PlatformConfig.xml", "r") as xp:
    xml_str = xmltodict.parse(xp.read())
    system_biosknobs_knob = xml_str["SYSTEM"]["biosknobs"]["knob"]
    for _key, _value in primaryParams.items():
        for _xml_item in system_biosknobs_knob:
            try:
                prompt_ = str(_xml_item["@prompt"]).lower()
                name_ = _xml_item["@name"]
                setup_type_ = _xml_item["@setupType"]
                if _key == prompt_:
                    # print(">>> key={}, value={}".format(_key, _value))
                    if setup_type_ == "oneof":
                        options_ = _xml_item["options"]["option"]
                        for _item in options_:
                            if _value == _item["@text"]:
                                print("<<< type={}, key={}, value={}".format(setup_type_, _key,
                                                                             _item["@value"]))
                                break
                    if setup_type_ == "numeric":
                        _value = hex(int(_value, 16))
                        print(
                            "<<< type={}, key={}, value={}".format(setup_type_, _key, str(_value)))
                        pass
            except Exception as e:
                pass

        pass

    pass
