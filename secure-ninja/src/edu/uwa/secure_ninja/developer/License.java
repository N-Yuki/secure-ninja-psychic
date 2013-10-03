/**
 * 
 */
package edu.uwa.secure_ninja.developer;

import java.net.InetAddress;

/**
 * @author wying1211
 *
 */
public class License {
	/**
	 * 
	 */
	private String licenseString;
	/**
	 * 
	 */
	private InetAddress softwareHouseIP;
	/**
	 * 
	 */
	private String libraryName;
	
	/**
	 * 
	 * @return
	 */
	protected String getLicenseString() {
		return licenseString;
	}
	
	/**
	 * 
	 * @param licenseString
	 */
	private void setLicenseString(String licenseString) {
		this.licenseString = licenseString;
	}
	
	/**
	 * 
	 * @return
	 */
	protected InetAddress getSoftwareHouseIP() {
		return softwareHouseIP;
	}
	
	/**
	 * 
	 * @param softwareHouseIP
	 */
	private void setSoftwareHouseIP(InetAddress softwareHouseIP) {
		this.softwareHouseIP = softwareHouseIP;
	}
	
	/**
	 * 
	 * @return
	 */
	protected String getLibraryName() {
		return libraryName;
	}
	
	/**
	 * 
	 * @param libraryName
	 */
	private void setLibraryName(String libraryName) {
		this.libraryName = libraryName;
	}

}
