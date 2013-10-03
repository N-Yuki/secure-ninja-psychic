/**
 * 
 */
package edu.uwa.secure_ninja.developer;

import java.io.File;
import java.net.InetAddress;
import java.util.List;

/**
 * 
 * @author Wan Ying GOH, Edwin TAY
 * 
 */
public interface IDeveloper {

	/**
	 * 
	 * @param numLicenses
	 * @param softwareHouseIP
	 * @return
	 */
	int requestLicenses(int numLicenses, InetAddress softwareHouseIP);

	/**
	 * 
	 * @param linkBrokerIP
	 * @param classFiles
	 * @param licenses
	 * @param JARName
	 * @return
	 */
	boolean linkFiles(InetAddress linkBrokerIP, List<File> classFiles,
			List<License> licenses, String JARName);
}
