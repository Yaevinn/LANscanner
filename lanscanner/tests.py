import pytest
import runpy
import scanner
import helperFunctions

# def test_test():
#     runpy.run_path('lanscanner/portScanner.py')
#     assert True

def test_scanner_publicDNS_8888():
    ipportMap = { 'ip': '8.8.8.8', 'port': 53 }
    assert scanner.portscan(ipportMap) == True

def test_helper_function_correct_list():
    textList = '80,443,90'
    assert helperFunctions.translateTextListToList(textList) == [80, 443, 90]

def test_helper_function_incorrect_list():
    textList = '80,443,90,xxx'
    assert helperFunctions.translateTextListToList(textList) == []

def test_ip_validate_correct():
    textIP = '127.0.0.1'
    assert helperFunctions.networkValidate(textIP) == True

def test_ip_validate_incorrect():
    textIP = '127.0.0.266'
    assert helperFunctions.networkValidate(textIP) == False

def test_network_validate_correct():
    textIP = '92.105.62.0/24'
    assert helperFunctions.networkValidate(textIP) == True

def test_network_validate_incorrect():
    textIP = '8.245.1.24/333'
    assert helperFunctions.networkValidate(textIP) == False