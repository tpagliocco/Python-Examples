import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys
import org.apache.commons.lang.RandomStringUtils as RandomStringUtils

protected String getSaltString() {
	String SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
	StringBuilder salt = new StringBuilder();
	Random rnd = new Random();
	while (salt.length() < 10) { // length of the random string.
		int index = (int) (rnd.nextFloat() * SALTCHARS.length());
		salt.append(SALTCHARS.charAt(index));
	}
	String saltStr = salt.toString();
	return saltStr;

}

int optionListLength = 0
Random rand = new Random()
int index = rand.nextInt(optionListLength + 1)

not_run: WebUI.openBrowser('')

WebUI.navigateToUrl('https://myodphi.omegadeltaphi.com/entity-reporting/')

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select a Report TypeBSR'), 'ESR', true)
//WebUI.selectOptionByIndex(findTestObject('Page_Entity Reporting  My ODPhi/select_Select a Report TypeBSR'), index)

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select a SemesterFallSp'), 'Spring', true)

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select a Year2018201920'), '2018', true)

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_next_button_1_7'))

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select your schoolAubur'), 'University of Washington', 
    true)

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select your regionCentr'), 'NW', true)

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select your entity clas'), 'Chapter', true)

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select your stateAlabam'), 'Washington', 
    true)

WebUI.selectOptionByValue(findTestObject('Page_Entity Reporting  My ODPhi/select_Select your semester st'), 'Quarter School', 
    true)

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_20.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_20.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_15'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_19.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_19.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_16'), getSaltString()+"@gmail.com")

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_next_button_1_17'))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_21.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_21.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_22'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_29.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_29.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_36'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_28.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_28.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_35'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_27.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_27.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_34'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_26.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_26.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_33'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_25.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_25.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_32'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_24.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_24.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_31'), getSaltString()+"@gmail.com")

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_23.3'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_23.6'), RandomStringUtils.randomAlphabetic(10))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_30'), getSaltString()+"@gmail.com")

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_next_button_1_37'))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_39'), RandomStringUtils.randomNumeric(2))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_45'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_44'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_43'), RandomStringUtils.randomNumeric(2))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_42'), RandomStringUtils.randomNumeric(2))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_41'), RandomStringUtils.randomNumeric(1))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/label_Personal  Family Issues'))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/label_Fraternities Not For The'))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/label_Grades  Academics'))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/label_Lack of Commitment'))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_next_button_1_48'))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_50'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_51'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_52'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_53'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_54'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_55'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_56'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_57'), RandomStringUtils.randomNumeric(1))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_next_button_1_58'))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_60'), '3.22')

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_61'), '3.50')

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_62'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_63'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_64'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_65'), '3.65')

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_66'), '3.22')

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_67'), RandomStringUtils.randomNumeric(1))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_next_button_1_69'))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_70'), RandomStringUtils.randomNumeric(3))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_71'), RandomStringUtils.randomNumeric(3))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_74'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_73'), RandomStringUtils.randomNumeric(4))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_75'), RandomStringUtils.randomNumeric(1))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_76'), RandomStringUtils.randomNumeric(4))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_78'), '0')

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_80'), RandomStringUtils.randomNumeric(5))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_81'), RandomStringUtils.randomNumeric(5))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_next_button_1_82'))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_84'), 'To do ABC')

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_85'), 'To do XYZ')

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/input_input_86'), 'To 123')

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/label_Dues Collection'))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/div_RecruitmentDues Collection'))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/label_Programming'))

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/label_National Board'))

WebUI.setText(findTestObject('Page_Entity Reporting  My ODPhi/textarea_input_88'), 'None')

WebUI.click(findTestObject('Page_Entity Reporting  My ODPhi/input_gform_submit_button_1'))

