$fcpPath = (Get-Location).Path + "\WSDATA.FCP"

$fcpFile = [System.IO.File]::ReadAllBytes($fcpPath)

$iterator = @"
	public class GetBytes {
		public static byte[] Add(byte[]fileArr, int startByte, int bytes) {
			byte[] localArr = new byte[bytes];
			int lastcount = 0;
			do {
				{
					int currentByte = lastcount + startByte;
					localArr[lastcount] = fileArr[currentByte];
				}
				lastcount++;
			} while (lastcount < bytes);
			return localArr;
		}
	}
"@
Add-Type -TypeDefinition $iterator

$fileList = 0x8
$currentOffset = $fileList
while ($fcpFile[$currentOffset]) {
	$fileName = ""
	0..11 | % {$fileName += [char]($fcpFile[$currentOffset+$_])}
	$address = ([int]$fcpFile[$currentOffset+13] -shl 24) + ([int]$fcpFile[$currentOffset+12] -shl 16) + ([int]$fcpFile[$currentOffset+15] -shl 8)+[int]$fcpFile[$currentOffset+14]
	$size = ([int]$fcpFile[$currentOffset+17] -shl 8)+[int]$fcpFile[$currentOffset+16]
	$unpackFile = [GetBytes]::Add($fcpFile, $address, ($size))
	[System.IO.File]::WriteAllBytes(((Get-Location).Path + "\" + $fileName.Replace(" ","")),$unpackFile)
	$currentOffset += 18
}