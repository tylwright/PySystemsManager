# PySystemsManager
A simple Python script used to SSH into boxes and complete tasks.

<img src='http://i.imgur.com/TEgTdax.gif' width='500px'/>
<figcaption>Example for Windows DHCP/DNS add host</figcaption>

<h3>Requirements</h3>
<ul>
	<li>Python</li>
	<li>Fabric for Python</li>
	<li>A Windows box with an SSH server running (if you would like to use the Windows features)</li>
</ul>

<h3>Running the script</h3>
Simply run main.py!  A menu of options will then be presented to you.

<h3>Script Capabilities</h3>
<table>
	<tr>
		<td>Windows</td>
		<td>
			<ul>
				<li>Add hosts to DHCP and/or DNS</li>
				<li>View DHCP reservations</li>
				<li>Add an AD user account</li>
				<li>Unlock or disable an AD user account</li>
				<li>View Hyper-V VMs</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>Linux</td>
		<td>
			<ul>
				<li>Restart services</li>
				<li>Restart or shutdown hosts</li>
			</ul>
		</td>
	</tr>
</table>

<h3>Notes</h3>
<ul>
	<li>For SSH on Windows, I have been using <a href='http://www.freesshd.com/?ctt=download'>freeSSHd</a>.
	<li>Make sure the fab_functions.py file is in the same directory as the main.py file.</li>
	<li>This script will <u>not</u> run without Fabric.</li>
</ul>